from typing import Any, Dict

import psutil

from src.collector.base_collector import BaseCollector
from src.helper.assistant import ByteUnitConverter


class RamCollector(BaseCollector):
    def __init__(self) -> None:
        super().__init__()

    def collect(self) -> Dict[Any, Any]:
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()  # get the swap memory details (if exists)
        self.json_output.setdefault(
            "Memory Information",
            {
                "Total": ByteUnitConverter.get_size(svmem.total),
                "Available": ByteUnitConverter.get_size(svmem.available),
                "Used": ByteUnitConverter.get_size(svmem.used),
                "Percentage": f"{svmem.percent}%",
                "SWAP": {
                    "Total": ByteUnitConverter.get_size(swap.total),
                    "Free": ByteUnitConverter.get_size(swap.free),
                    "Used": ByteUnitConverter.get_size(swap.used),
                    "Percentage": f"{swap.percent}%",
                },
            },
        )
        return self.json_output
