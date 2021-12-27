from typing import List

from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import Category, CategoryDescriptors
from app.collector.hardware.cpu_descriptor import CpuDescriptor
from app.collector.hardware.harddrive_descriptor import HarddriveDescriptor
from app.collector.hardware.ram_descriptor import RamDescriptor
from app.collector.network.interface_descriptor import InterfaceDescriptor
from app.collector.network.ssid_descriptor import SsidDescriptor
from app.collector.process.pid_descriptor import PidDescriptor
from app.collector.software.installed_software_descriptor import (
    InstalledSoftwareDescriptor,
)
from app.collector.software.startup_software_descriptor import StartupSoftwareDescriptor
from app.collector.uncategorized.system_descriptor import SystemDescriptor


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
