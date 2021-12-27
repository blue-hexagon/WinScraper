from dataclasses import dataclass


@dataclass
class Category:
    name: str
    cmd_arg: str
    parameter: str
    description: str


class CategoryDescriptors:
    ALL = Category(name="Everything", cmd_arg="--all", parameter="all", description="All modules (everything)")
    HARDWARE = Category(name="Hardware", cmd_arg="--hardware", parameter="hardware", description="All hardware modules")
    NETWORK = Category(name="Network", cmd_arg="--network", parameter="network", description="All network modules")
    PROCESS = Category(name="Process", cmd_arg="--process", parameter="process", description="All process modules")
    SOFTWARE = Category(name="Software", cmd_arg="--software", parameter="software", description="All software modules")
    UNCATEGORIZED = Category(
        name="Uncategorized",
        cmd_arg="--uncategorized",
        parameter="uncategorized",
        description="All uncategorized modules",
    )
    ALL_CATEGORIES = [
        ALL,
        HARDWARE,
        NETWORK,
        PROCESS,
        SOFTWARE,
        UNCATEGORIZED,
    ]
