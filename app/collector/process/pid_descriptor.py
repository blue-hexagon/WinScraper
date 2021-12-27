from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import CategoryDescriptors
from app.collector.process.pid import PidCollector


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
