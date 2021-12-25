from typing import Any, Dict

import wmi

from app.collector.base_collector import BaseCollector
from app.collector.collection_category import CollectionCategory


class PIDCollector(BaseCollector):
    def __init__(self) -> None:
        super().__init__(
            name="Process ID Collector",
            description="Collects all process names and IDs",
            category=CollectionCategory.PROCESS,
            cmd_arg="--pid",
        )

    def collect(self) -> Dict[Any, Any]:
        f = wmi.WMI()
        self.json_output.setdefault("Process List", {})
        for process in f.Win32_Process():
            try:
                self.json_output["Process List"][process.Name].append(process.ProcessId)
            except KeyError:
                self.json_output["Process List"][process.Name] = []
                self.json_output["Process List"][process.Name].append(process.ProcessId)

        return self.json_output
