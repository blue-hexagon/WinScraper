import ctypes
import getpass
import os
import platform
from traceback import print_exc
from typing import Any, Dict

import wmi

from app.collector.base_collector import BaseCollector
from app.collector.collection_category import CollectionCategory


class SystemCollector(BaseCollector):
    def __init__(self) -> None:
        super().__init__(
            name="System Information Collector",
            description="Collect device and system information",
            category=CollectionCategory.UNCATEGORIZED,
            cmd_arg="--system",
        )
        self.c = wmi.WMI()
        self.device = self.c.Win32_ComputerSystem()[0]

    def collect(self) -> Dict[Any, Any]:
        uname = platform.uname()

        self.json_output.setdefault(
            "System",
            {
                **self.collect_from_subprocess(),
                "OS Name": self.c.Win32_OperatingSystem()[0].Caption,
                "Node Name": uname.node,
                "Current User": getpass.getuser(),
                "Admin Privileges": self.user_is_admin(),
                "Machine": uname.machine,
                "Processor": uname.processor,
                "Platform Info": {
                    "Architecture": platform.architecture(),
                    "Python Build": platform.python_build(),
                    "Python Compiler": platform.python_compiler(),
                    "Python Implementation": platform.python_implementation(),
                    "Python Version": platform.python_version(),
                },
            },
        )
        return self.json_output

    @staticmethod
    def user_is_admin() -> bool:
        if os.name.lower() == "nt":
            try:
                return bool(ctypes.windll.shell32.IsUserAnAdmin())
            except Exception:  # TODO: Too broad
                print_exc()
                print("Admin check failed, assuming not an admin.")
                return False
        else:
            raise RuntimeError(f"Unsupported operating system for this module: {os.name}")

    @staticmethod
    def collect_from_subprocess() -> Dict[Any, Any]:
        import subprocess

        subprocess_call = subprocess.check_output(["systeminfo"]).decode("utf-8").split("\n")
        items: Dict[Any, Any] = {}
        for item in subprocess_call:
            try:
                if item.startswith(" "):
                    continue
                if (
                    item.startswith("Processor(s)")
                    or item.startswith("Host Name")
                    or item.startswith("Total Physical Memory")
                    or item.startswith("Available Physical Memory")
                    or item.startswith("Virtual Memory")
                    or item.startswith("Network Card(s)")
                    or item.startswith("Hotfix(s)")
                    or item.startswith("Hyper-V Requirements")
                ):
                    # TODO: Rework method to include arrays of e.g. hotfixes
                    continue
                k, v = item.split(":", maxsplit=1)
                items.setdefault(str(k).strip(), str(v).strip())
            except ValueError:
                continue
        return items
