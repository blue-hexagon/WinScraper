from app.collector.base_objs import BaseDescriptor
from app.collector.collections_enum import EnumerationCategories


class SystemDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="System Information Collector",
            description="Collect device and system information",
            category=EnumerationCategories.UNCATEGORIZED,
            cmd_arg="--system",
            parameter="system",
        )
