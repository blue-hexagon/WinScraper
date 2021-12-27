import argparse

from app.helper.descriptor_helper import Descriptors
from app.view.help import HelpView
from app.view.winscraper import WinScraper

if __name__ == "__main__":
    if CLI := True:

        parser = argparse.ArgumentParser("Collect a plethora of information about this device.")
        for descriptor in Descriptors.all_descriptors:
            parser.add_argument(descriptor.cmd_arg, help=descriptor.description, action="store_true")
        for category in Descriptors.all_categories:
            parser.add_argument(category.cmd_arg, help=category.description, action="store_true")
        args = parser.parse_args()
        WinScraper(**vars(args)).print()
    else:
        sysinfo = WinScraper()
        sysinfo.print()
        HelpView.display()
