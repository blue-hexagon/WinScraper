import aenum as aenum


class EnumerationCategories(aenum.Constant):
    ALL = ("Everything", "--all", "all", "All modules (everything)")
    HARDWARE = ("Hardware", "--hardware", "hardware", "All hardware modules")
    NETWORK = ("Network", "--network", "network", "All network modules")
    PROCESS = ("Process", "--process", "process", "All process modules")
    SOFTWARE = ("Software", "--software", "software", "All software modules")
    UNCATEGORIZED = ("Uncategorized", "--uncategorized", "uncategorized", "All uncategorized modules")
