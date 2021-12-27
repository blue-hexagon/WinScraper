from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import CategoryDescriptors
from app.collector.hardware.harddrive import HarddriveCollector


class HarddriveDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="Harddrive Collector",
            description="Collects information about disks and partitions as well as their usage",
            category=CategoryDescriptors.HARDWARE,
            cmd_arg="--harddrive",
            parameter="harddrive",
            collector=HarddriveCollector,
        )
