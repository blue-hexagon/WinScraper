from typing import Any, Dict, Tuple


class BaseDescriptor:
    def __init__(self, name: str, description: str, category: Tuple[str, str, str, str], cmd_arg: str, parameter: str):
        self.name: str = name
        self.description: str = description
        self.category: Tuple[str, str, str, str] = category
        self.cmd_arg: str = cmd_arg
        self.parameter: str = parameter
        self.json_output: Dict[Any, Any] = {}
