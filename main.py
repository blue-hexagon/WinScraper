from app.help_view import HelpView
from app.winscraper import WinScraper

if __name__ == "__main__":
    sysinfo = WinScraper(system=True)
    sysinfo.print()
    HelpView.display()
