from typing import Any, Dict

import wmi

from app.collector.base_objs import BaseCollector


class PidCollector(BaseCollector):
    def __init__(self) -> None:
        super().__init__()

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
