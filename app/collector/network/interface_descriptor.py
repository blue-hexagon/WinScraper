from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import EnumerationCategories


class InterfaceDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="Network Interface Collector",
            description="Collects information about the devices network adapters, assigned IP addresses, MAC addresses and more",
            category=EnumerationCategories.NETWORK,
            cmd_arg="--net",
            parameter="net",
        )
