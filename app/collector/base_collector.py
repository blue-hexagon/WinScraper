from typing import Any, Dict


class BaseCollector:
    def __init__(self) -> None:
        self.json_output: Dict[Any, Any] = {}

    def collect(self) -> Dict[Any, Any]:
        ...
