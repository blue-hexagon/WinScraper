from src.collector.base_descriptor import BaseDescriptor
from src.collector.category_descriptor import CategoryDescriptors
from src.collector.hardware.cpu import CpuCollector


class CpuDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="CPU Collector",
            description="Gathers information about the CPU such as the number of cores and their utilization",
            category=CategoryDescriptors.HARDWARE,
            cmd_arg="--cpu",
            parameter="cpu",
            collector=CpuCollector,
        )
