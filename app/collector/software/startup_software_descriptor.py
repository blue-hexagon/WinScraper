from app.collector.base_objs import BaseDescriptor
from app.collector.collections_enum import EnumerationCategories


class StartupSoftwareDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="Startup Software Collector",
            description="Scan the windows registry for software which is executed at startup",
            category=EnumerationCategories.SOFTWARE,
            cmd_arg="--startup-software",
            parameter="startup_software",
        )
