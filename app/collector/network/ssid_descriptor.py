from app.collector.base_objs import BaseDescriptor
from app.collector.collections_enum import EnumerationCategories


class SsidDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="SSID Collector",
            description="Collects saved SSID and their associated passwords if such exists",
            category=EnumerationCategories.NETWORK,
            cmd_arg="--ssid",
            parameter="ssid",
        )
