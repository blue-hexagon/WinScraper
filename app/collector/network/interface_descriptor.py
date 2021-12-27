from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import CategoryDescriptors
from app.collector.network.interface import InterfaceCollector


class InterfaceDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="Network Interface Collector",
            description="Collects information about the devices network adapters, assigned IP addresses, MAC addresses and more",
            category=CategoryDescriptors.NETWORK,
            cmd_arg="--interface",
            parameter="interface",
            collector=InterfaceCollector,
        )
