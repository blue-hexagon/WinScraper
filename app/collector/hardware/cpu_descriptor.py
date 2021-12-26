from app.collector.base_objs import BaseDescriptor
from app.collector.collections_enum import EnumerationCategories


class CpuDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="CPU Collector",
            description="Gathers information about the CPU such as the number of cores and their utilization",
            category=EnumerationCategories.HARDWARE,
            cmd_arg="--cpu",
            parameter="cpu",
        )
