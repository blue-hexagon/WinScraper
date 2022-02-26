import argparse
import sys
from typing import Dict

from src.helper.descriptor_helper import Descriptors
from src.view.application import ApplicationView


class WinScraper:
    """
    Display CLI Arguments
        From the commandline, run: python winscraper.py -h

    Display Object Kwargs
        From the commandline, run: python winscraper.py

    CLI Usage
        python winscraper.py --system --ssid --startup-software

    Object Usage
        WinScraper(all=True, software=False, ssid=False)

    Other Parameters
        formatting="json"

        formatting="yaml"
    """

    def __init__(self, formatting: str = "json", **kwargs: Dict[str, bool] | bool) -> None:
        if sys.stdin and sys.stdin.isatty():
            parser = argparse.ArgumentParser(
                "Collect a plethora of information about this device and everything related to it."
            )
            for descriptor in Descriptors.all_descriptors:
                parser.add_argument(descriptor.cmd_arg, help=descriptor.description, action="store_true")
            for category in Descriptors.all_categories:
                parser.add_argument(category.cmd_arg, help=category.description, action="store_true")
            args = parser.parse_args()
            ApplicationView(formatting=formatting, **vars(args)).print()
        else:
            for descriptor in Descriptors.all_descriptors:
                if descriptor.parameter not in kwargs:
                    kwargs.setdefault(descriptor.parameter, False)
            for category in Descriptors.all_categories:
                if category.parameter not in kwargs:
                    kwargs.setdefault(category.parameter, False)
            ApplicationView(formatting=formatting, **kwargs).print()
