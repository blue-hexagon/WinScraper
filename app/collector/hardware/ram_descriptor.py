from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import EnumerationCategories


class RamDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="RAM Collector",
            description="Collects information about the devices RAM consumption and resources",
            category=EnumerationCategories.HARDWARE,
            cmd_arg="--ram",
            parameter="ram",
        )
