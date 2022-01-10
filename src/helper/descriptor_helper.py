from typing import List

from src.collector.base_descriptor import BaseDescriptor
from src.collector.category_descriptor import Category, CategoryDescriptors
from src.collector.hardware.cpu_descriptor import CpuDescriptor
from src.collector.hardware.harddrive_descriptor import HarddriveDescriptor
from src.collector.hardware.ram_descriptor import RamDescriptor
from src.collector.network.interface_descriptor import InterfaceDescriptor
from src.collector.network.ssid_descriptor import SsidDescriptor
from src.collector.process.pid_descriptor import PidDescriptor
from src.collector.software.installed_software_descriptor import (
    InstalledSoftwareDescriptor,
)
from src.collector.software.startup_software_descriptor import StartupSoftwareDescriptor
from src.collector.uncategorized.system_descriptor import SystemDescriptor


class Descriptors:
    all_descriptors = [
        SystemDescriptor(),
        CpuDescriptor(),
        RamDescriptor(),
        HarddriveDescriptor(),
        InterfaceDescriptor(),
        SsidDescriptor(),
        StartupSoftwareDescriptor(),
        InstalledSoftwareDescriptor(),
        PidDescriptor(),
    ]
    all_categories = CategoryDescriptors.ALL_CATEGORIES

    @classmethod
    def get_all_descriptors(cls) -> List[BaseDescriptor]:
        return cls.all_descriptors

    @classmethod
    def get_all_categories(cls) -> List[Category]:
        return cls.all_categories
