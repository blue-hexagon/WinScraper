import json
from typing import Any, Dict, List

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


class SimpleDiner:
    all_modules = [
        SystemCollector(),
        CPUCollector(),
        MemoryCollector(),
        DiskCollector(),
        NetworkInterfaceCollector(),
        LANPasswordLister(),
        StartupProgramsCollector(),
        SoftwareRegeditLister(),
        PIDCollector(),
    ]

    def __init__(
        self,
        collect_everything: bool = False,
        system_information: bool = False,
        running_processes: bool = False,
        cpu_information: bool = False,
        disk_information: bool = False,
        memory_information: bool = False,
        network_interfaces: bool = False,
        get_startup_programs: bool = False,
        ssid_password_lister: bool = False,
        installed_software: bool = False,
    ) -> None:

        self.collection = []
        bucket: List[Any] = []
        self.collectors: Dict[Any, Any] = {}
        if system_information or collect_everything:
            bucket.append(SystemCollector())
        if cpu_information or collect_everything:
            bucket.append(CPUCollector())
        if memory_information or collect_everything:
            bucket.append(MemoryCollector())
        if disk_information or collect_everything:
            bucket.append(DiskCollector())
        if network_interfaces or collect_everything:
            bucket.append(NetworkInterfaceCollector())
        if ssid_password_lister or collect_everything:
            bucket.append(LANPasswordLister())
        if get_startup_programs or collect_everything:
            bucket.append(StartupProgramsCollector())
        if running_processes or collect_everything:
            bucket.append(PIDCollector())
        if installed_software or collect_everything:
            bucket.append(SoftwareRegeditLister())
        if len(bucket) == 0:
            raise KeyError("No collector selected. You must set at least one named parameter to True.")

        for collector in bucket:
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
            for idy, module in enumerate(cls.all_modules, start=1):  # TODO: O^2
                if module.category[0] == category[0]:
                    print(
                        f"{str(idx) + '.' + str(idy):<{id_field_len}} {module.name:<{name_field_len}}{module.cmd_arg:<{cmd_field_len}}{module.description}"
                    )
            print()

    def print(self) -> None:
        print(json.dumps(self.collection, indent=2, ensure_ascii=True))
