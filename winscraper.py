import sys

from src.main import WinScraper


def main() -> int:
    try:
        WinScraper()
        return 0
    except Exception:
        return 1


if __name__ == "__main__":
    """Run `python winscraper.py -h` for information about commandline usage"""
    """ Run `python winscraper.py` for information about library usage """
    sys.exit(main())
