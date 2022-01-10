from typing import Any, Dict

import psutil

from src.collector.base_collector import BaseCollector


class CpuCollector(BaseCollector):
    def __init__(self) -> None:
        super().__init__()

    def collect(self) -> Dict[Any, Any]:
        cpufreq = psutil.cpu_freq()
        cpu_usage_per_core = {}
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            cpu_usage_per_core[f"Core {i + 1}"] = f"{percentage}%"
        self.json_output.setdefault(
            "CPU Information",
            {
                "Physical Cores": psutil.cpu_count(logical=False),
                "Total Cores": psutil.cpu_count(logical=True),
                "Max Frequency": f"{cpufreq.max:.2f}Mhz",
                "Min Frequency": f"{cpufreq.min:.2f}Mhz",
                "Current Frequency": f"{cpufreq.current:.2f}Mhz",
                "Core Usage": cpu_usage_per_core,
                "Total CPU Usage": f"{psutil.cpu_percent()}%",
            },
        )
        return self.json_output
