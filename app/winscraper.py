import json
from typing import Any, List

from app.app_assistant import TextFileSaver
from app.collector.hardware.cpu import CpuCollector
from app.collector.hardware.harddrive import HarddriveCollector
from app.collector.hardware.ram import RamCollector
from app.collector.network.interface import InterfaceCollector
from app.collector.network.ssid import SsidCollector
from app.collector.process.pid import PidCollector
from app.collector.software.installed_software import InstalledSoftwareCollector
from app.collector.software.startup_software import StartupSoftwareCollector
from app.collector.uncategorized.system import SystemCollector


class WinScraper:
    def __init__(
        self,
        all: bool = False,
        hardware: bool = False,
        network: bool = False,
        process: bool = False,
        software: bool = False,
        uncategorized: bool = False,
        system: bool = False,
        pid: bool = False,
        cpu: bool = False,
        harddrive: bool = False,
        ram: bool = False,
        interface: bool = False,
        startup_software: bool = False,
        ssid: bool = False,
        installed_software: bool = False,
    ) -> None:

        self.bucket: List[Any] = []
        if system or uncategorized or all:
            self.bucket.append(SystemCollector())
        if cpu or hardware or all:
            self.bucket.append(CpuCollector())
        if ram or hardware or all:
            self.bucket.append(RamCollector())
        if harddrive or hardware or all:
            self.bucket.append(HarddriveCollector())
        if interface or network or all:
            self.bucket.append(InterfaceCollector())
        if ssid or network or all:
            self.bucket.append(SsidCollector())
        if startup_software or software or all:
            self.bucket.append(StartupSoftwareCollector())
        if pid or process or all:
            self.bucket.append(PidCollector())
        if installed_software or software or all:
            self.bucket.append(InstalledSoftwareCollector())
        if len(self.bucket) == 0:
            raise KeyError("No collector selected. You must set at least one named parameter to True.")

        self.collection = []
        for collector in self.bucket:
            self.collection.append(collector.collect())

    def save(self) -> None:
        TextFileSaver.save_as_text(*self.collection)

    def print(self) -> None:
        print(json.dumps(self.collection, indent=2, ensure_ascii=True))
