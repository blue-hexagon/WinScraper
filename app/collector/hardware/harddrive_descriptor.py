from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import EnumerationCategories


class HarddriveDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="Harddrive Collector",
            description="Collects information about disks and partitions as well as their usage",
            category=EnumerationCategories.HARDWARE,
            cmd_arg="--disk",
            parameter="disk",
        )
