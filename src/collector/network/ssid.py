import platform
import subprocess
from typing import Any, Dict

from src.collector.base_collector import BaseCollector


class SsidCollector(BaseCollector):
    def __init__(self) -> None:
        super().__init__()

    def collect(self) -> Dict[Any, Any]:
        if not platform.uname().system.lower() == "windows":
            raise OSError("Requires the Windows operating system")
        ssid_pw_map: Dict[Any, Any] = {}
        data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("cp1140").split("\n")
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        # FIXME: Weird encoding issues causes data to be rendered as encoded string
        for ssid in profiles:
            results = (
                subprocess.check_output(["netsh", "wlan", "show", "profiles", ssid, "key=clear"])
                .decode("cp1140")
                .split("\n")
            )
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                ssid_pw_map.setdefault(ssid, results[0])
            except IndexError:
                ssid_pw_map.setdefault(ssid, "None")
        return {"SSID Password": ssid_pw_map}
