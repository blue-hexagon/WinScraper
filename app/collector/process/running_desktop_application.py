from pywinauto import Desktop

from app.collector.base_collector import BaseCollector
from app.collector.collection_category import CollectionCategory


class RunningDesktopApplicationCollector(BaseCollector):
    def __init__(self) -> None:
        super().__init__(
            name="Running Desktop Application Collector",
            description="Collect the users opened application window titles",
            category=CollectionCategory.PROCESS,
            cmd_arg="--running-windows",
        )


if __name__ == "__main__":
    windows = Desktop(backend="uia").windows()
    for w in windows:
        print(w.window_text())
