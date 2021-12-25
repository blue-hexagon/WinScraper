import winreg
from typing import Any, Dict

from app.collector.base_collector import BaseCollector
from app.collector.collection_category import CollectionCategory


class SoftwareRegeditLister(BaseCollector):
    def __init__(self) -> None:
        super().__init__(
            name="Installed Software Collector",
            description="...",
            category=CollectionCategory.SOFTWARE,
            cmd_arg="--installed-software",
        )

    def collect(self) -> Dict[Any, Any]:
        access_keys = [
            winreg.OpenKey(winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER), r"SOFTWARE"),
            winreg.OpenKey(winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE), r"SOFTWARE"),
            winreg.OpenKey(winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE), r"SOFTWARE\\WOW6432Node"),
        ]
        software = set()
        for key in access_keys:
            idx = -1
            while True:
                try:
                    software.add(winreg.EnumKey(key, idx := idx + 1))
                except OSError:
                    break
        return {"Software List from Windows Registry": list(sorted(software))}


# def firefox_version():
#     try:
#         version = get_registry_value(
#             "HKEY_LOCAL_MACHINE",
#             "SOFTWARE\\Mozilla\\Mozilla Firefox",
#             "CurrentVersion")
#         version = (u"Mozilla Firefox", version)
#     except WindowsError:
#         version = None
#     return version
#
#
# def iexplore_version():
#     try:
#         version = get_registry_value(
#             "HKEY_LOCAL_MACHINE",
#             "SOFTWARE\\Microsoft\\Internet Explorer",
#             "Version")
#         version = (u"Internet Explorer", version)
#     except WindowsError:
#         version = None
#     return version
#
#
# def browsers():
#     browsers = []
#     firefox = firefox_version()
#     if firefox:
#         browsers.append(firefox)
#     iexplore = iexplore_version()
#     if iexplore:
#         browsers.append(iexplore)
#
#     return browsers
#
