import aenum as aenum


class CollectionCategory(aenum.Constant):
    HARDWARE = ("Hardware", "--hardware", "All information regarding the hardware on the device")
    NETWORK = ("Network", "--network", "All information regarding network adapters, interfaces and more")
    PROCESS = ("Process", "--process", "All information regarding processes running on Windows")
    SOFTWARE = ("Software", "--software", "All information regarding software installed or running on Windows")
    UNCATEGORIZED = (
        "Uncategorized",
        "--uncategorized",
        "All information that doesn't precisely fit into any other category",
    )
