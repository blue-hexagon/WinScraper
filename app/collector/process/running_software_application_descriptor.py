from app.collector.base_objs import BaseDescriptor
from app.collector.collections_enum import EnumerationCategories


class RunningDesktopApplicationDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="Running Desktop Application Collector",
            description="Collect the users opened application window titles",
            category=EnumerationCategories.PROCESS,
            cmd_arg="--running-windows",
            parameter="running_windows",
        )
