from src.collector.base_descriptor import BaseDescriptor
from src.collector.category_descriptor import CategoryDescriptors
from src.collector.hardware.ram import RamCollector


class RamDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="RAM Collector",
            description="Collects information about the devices RAM consumption and resources",
            category=CategoryDescriptors.HARDWARE,
            cmd_arg="--ram",
            parameter="ram",
            collector=RamCollector,
        )
