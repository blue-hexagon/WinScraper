import argparse
import sys
from typing import Dict

from src.helper.descriptor_helper import Descriptors
from src.view.application import ApplicationView


class WinScraper:
    def __init__(self, **kwargs: Dict[str, bool] | bool) -> None:
        if sys.stdin and sys.stdin.isatty():
            parser = argparse.ArgumentParser(
                "Collect a plethora of information about this device and everything related to it."
            )
            for descriptor in Descriptors.all_descriptors:
                parser.add_argument(descriptor.cmd_arg, help=descriptor.description, action="store_true")
            for category in Descriptors.all_categories:
                parser.add_argument(category.cmd_arg, help=category.description, action="store_true")
            args = parser.parse_args()
            ApplicationView(**vars(args)).print()
        else:
            ApplicationView(**kwargs).print()
