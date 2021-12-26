from app.collector.base_descriptor import BaseDescriptor
from app.collector.category_descriptor import EnumerationCategories


class RunningDesktopApplicationDescriptor(BaseDescriptor):
    def __init__(self) -> None:
        super().__init__(
            name="Running Desktop Application Collector",
            description="Collect the users opened application window titles",
            category=EnumerationCategories.PROCESS,
            cmd_arg="--running-windows",
            parameter="running_windows",
        )
