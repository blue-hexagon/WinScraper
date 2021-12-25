import platform
import subprocess
from typing import Any, Dict

from app.collector.base_collector import BaseCollector
from app.collector.collection_category import CollectionCategory


class LANPasswordLister(BaseCollector):
    def __init__(self) -> None:
        super().__init__(
            name="SSID Collector",
            description="Collects saved SSID and their associated passwords if such exists",
            category=CollectionCategory.NETWORK,
            cmd_arg="--ssid",
        )

    def collect(self) -> Dict[Any, Any]:
        if not platform.uname().system.lower() == "windows":
            raise OSError("Requires the Windows operating system")
        ssid_pw_map: Dict[Any, Any] = {}  # TODO: What's the type??
        data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for ssid in profiles:
            results = (
                subprocess.check_output(["netsh", "wlan", "show", "profile", ssid, "key=clear"])
                .decode("utf-8")
                .split("\n")
            )
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                ssid_pw_map.setdefault(ssid, results[0])
            except IndexError:
                ssid_pw_map.setdefault(ssid, "None")
        return {"SSID Password": ssid_pw_map}
