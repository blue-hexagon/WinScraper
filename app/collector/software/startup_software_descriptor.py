from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import CategoryDescriptors
from app.collector.software.startup_software import StartupSoftwareCollector


class StartupSoftwareDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="Startup Software Collector",
            description="Scan the windows registry for software which is executed at startup",
            category=CategoryDescriptors.SOFTWARE,
            cmd_arg="--startup-software",
            parameter="startup_software",
            collector=StartupSoftwareCollector,
        )
