from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import CategoryDescriptors
from app.collector.network.ssid import SsidCollector


class SsidDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="SSID Collector",
            description="Collects saved SSID and their associated passwords if such exists",
            category=CategoryDescriptors.NETWORK,
            cmd_arg="--ssid",
            parameter="ssid",
            collector=SsidCollector,
        )
