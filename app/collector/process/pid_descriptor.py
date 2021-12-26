from app.collector.base_objs import BaseDescriptor
from app.collector.collections_enum import EnumerationCategories


class PidDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="Process ID Collector",
            description="Collects all process names and IDs",
            category=EnumerationCategories.PROCESS,
            cmd_arg="--pid",
            parameter="pid",
        )
