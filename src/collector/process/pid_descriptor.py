from src.collector.base_descriptor import BaseDescriptor
from src.collector.category_descriptor import CategoryDescriptors
from src.collector.process.pid import PidCollector


class PidDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="Process ID Collector",
            description="Collects all process names and IDs",
            category=CategoryDescriptors.PROCESS,
            cmd_arg="--pid",
            parameter="pid",
            collector=PidCollector,
        )
