from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import CategoryDescriptors
from app.collector.uncategorized.system import SystemCollector


class SystemDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="System Information Collector",
            description="Collect device and system information",
            category=CategoryDescriptors.UNCATEGORIZED,
            cmd_arg="--system",
            parameter="system",
            collector=SystemCollector,
        )
