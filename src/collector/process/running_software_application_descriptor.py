from src.collector.base_descriptor import BaseDescriptor
from src.collector.category_descriptor import CategoryDescriptors
from src.collector.process.running_desktop_application import (
    RunningDesktopApplicationCollector,
)


class RunningDesktopApplicationDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="Running Desktop Application Collector",
            description="Collect the users opened application window titles",
            category=CategoryDescriptors.PROCESS,
            cmd_arg="--running-windows",
            parameter="running_windows",
            collector=RunningDesktopApplicationCollector,
        )
