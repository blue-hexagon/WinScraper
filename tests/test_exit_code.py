import unittest

from src.winscraper import WinScraper


class TestRunsWithoutErrors(unittest.TestCase):
    @staticmethod
    def get_exit_code():
        try:
            WinScraper(all=True, formatting="json")
            WinScraper(all=True, formatting="yaml")
            return 0
        except Exception("Something unaccounted for happended"):
            return 1

    def test_run(self):
        self.assertEqual(self.get_exit_code(), 0, "Exit code should be 0")


if __name__ == "__main__":
    unittest.main()
