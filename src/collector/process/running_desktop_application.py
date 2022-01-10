from pywinauto import Desktop

from src.collector.base_collector import BaseCollector


class RunningDesktopApplicationCollector(BaseCollector):
    def __init__(self) -> None:
        super().__init__()


if __name__ == "__main__":
    windows = Desktop(backend="uia").windows()
    for w in windows:
        print(w.window_text())
