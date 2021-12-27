from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import CategoryDescriptors
from app.collector.software.installed_software import InstalledSoftwareCollector


class InstalledSoftwareDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="Installed Software Collector",
            description="Scan the windows registry for installed software",
            category=CategoryDescriptors.SOFTWARE,
            cmd_arg="--installed-software",
            parameter="installed_software",
            collector=InstalledSoftwareCollector,
        )
