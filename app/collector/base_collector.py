from typing import Any, Dict, Tuple


class BaseCollector:
    def __init__(self, name: str, description: str, category: Tuple[str, str, str], cmd_arg: str):
        self.name: str = name
        self.description: str = description
        self.category: Tuple[str, str, str] = category
        self.cmd_arg: str = cmd_arg
        self.json_output: Dict[Any, Any] = {}

    def collect(self) -> Dict[Any, Any]:
        ...
