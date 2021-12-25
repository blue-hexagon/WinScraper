import json
from typing import Any, List

from app.app_assister import TextFileSaver
from app.collector.collection_category import CollectionCategory
from app.collector.hardware.cpu import CPUCollector
from app.collector.hardware.harddrive import DiskCollector
from app.collector.hardware.ram import MemoryCollector
from app.collector.network.network_interface import NetworkInterfaceCollector
from app.collector.network.stored_ssid import LANPasswordLister
from app.collector.process.pid import PIDCollector
from app.collector.software.installed_software import SoftwareRegeditLister
from app.collector.software.startup_software import StartupProgramsCollector
from app.collector.uncategorized.system import SystemCollector


class Diner:
    all_modules = {
        "system": SystemCollector(),
        "cpu": CPUCollector(),
        "ram": MemoryCollector(),
        "disk": DiskCollector(),
        "network": NetworkInterfaceCollector(),
        "ssid": LANPasswordLister(),
        "startup_software": StartupProgramsCollector(),
        "installed_software": SoftwareRegeditLister(),
        "pid": PIDCollector(),
    }

    def __init__(
        self,
        all: bool = False,
        system: bool = False,
        pid: bool = False,
        cpu: bool = False,
        disk: bool = False,
        ram: bool = False,
        network: bool = False,
        startup_software: bool = False,
        ssid: bool = False,
        installed_software: bool = False,
    ) -> None:

        self.bucket: List[Any] = []
        if system or all:
            self.bucket.append(Diner.all_modules["system"])
        if cpu or all:
            self.bucket.append(Diner.all_modules["cpu"])
        if ram or all:
            self.bucket.append(Diner.all_modules["ram"])
        if disk or all:
            self.bucket.append(Diner.all_modules["disk"])
        if network or all:
            self.bucket.append(Diner.all_modules["network"])
        if ssid or all:
            self.bucket.append(Diner.all_modules["ssid"])
        if startup_software or all:
            self.bucket.append(Diner.all_modules["startup_software"])
        if pid or all:
            self.bucket.append(Diner.all_modules["pid"])
        if installed_software or all:
            self.bucket.append(Diner.all_modules["installed_software"])
        if len(self.bucket) == 0:
            raise KeyError("No collector selected. You must set at least one named parameter to True.")

        self.collection = []
        for collector in self.bucket:
            self.collection.append(collector.collect())

    def save(self) -> None:
        TextFileSaver.save_as_text(*self.collection)

    @classmethod
    def help(cls) -> None:
        """
        Just a bunch of string formatting for displaying a help menu showcasing an ID, the collector's names,
        CLI arguments and descriptions (in that order).
        """
        id_field_len, name_field_len, cmd_field_len = (
            4,
            32,
            24,
        )  # The final description field just occupies whatever space is left # noqa
        for idx, category in enumerate(CollectionCategory, start=1):  # type: ignore
            print(
                f"{str(idx) + '.':<{id_field_len}} {category[0]:<{name_field_len}}{category[1]:<{cmd_field_len}}{category[2]}"
            )  # noqa
            idy = 0  # For some reason enumerate doesn't reset it's (idy) counter when finishing the loop and starting over, so we do it the old way
            for module in cls.all_modules.values():  # TODO: O^2
                if module.category[0] == category[0]:
                    idy += 1
                    print(
                        f"{str(idx) + '.' + str(idy):<{id_field_len}} {module.name:<{name_field_len}}{module.cmd_arg:<{cmd_field_len}}{module.description}"
                    )
            print()

    def print(self) -> None:
        print(json.dumps(self.collection, indent=2, ensure_ascii=True))
