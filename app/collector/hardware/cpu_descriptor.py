from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import CategoryDescriptors
from app.collector.hardware.cpu import CpuCollector


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
