from typing import Any, Callable, Dict

from src.collector.category_descriptor import Category


class BaseDescriptor:
    def __init__(
        self,
        name: str,
        description: str,
        category: Category,
        cmd_arg: str,
        parameter: str,
        collector: Callable,  # type: ignore
    ):
        self.name: str = name
        self.description: str = description
        self.category: Category = category
        self.cmd_arg: str = cmd_arg
        self.parameter: str = parameter
        self.collector: Callable = collector  # type: ignore
        self.json_output: Dict[Any, Any] = {}
