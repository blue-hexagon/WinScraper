import json
import logging
import os
import sys
from datetime import datetime
from typing import Any, Dict


class DateTimeFormatter:
    @staticmethod
    def current_dt() -> str:
        return datetime.now().strftime("%c")

    @classmethod
    def current_dt_fileformatted(cls) -> str:
        return cls.current_dt().replace(" ", "_").replace(":", "-")


class ByteUnitConverter:
    @staticmethod
    def get_size(byte_count: float, suffix: str = "B") -> str | None:  # type: ignore
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor: float = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if byte_count < factor:
                return f"{byte_count:.2f}{unit}{suffix}"
            byte_count /= factor


class TextFileSaver:
    BASE_DIR = r"./output"

    @classmethod
    def save_as_text(cls, dictionary: Dict[Any, Any]) -> None:
        TextFileSaver.save(f_prefix="enum", text=json.dumps(dictionary))

    @classmethod
    def save(cls, f_prefix: str, text: str | bytes) -> None:
        if type(text) == type(bytes):
            try:
                text = text.decode("utf-8")  # type: ignore
            except (UnicodeDecodeError, AttributeError):
                logging.getLogger().error("Failed to decode bytes object")
                sys.exit(0)
        with open(os.path.join(cls.BASE_DIR, f_prefix + "-" + DateTimeFormatter.current_dt_fileformatted()), "w+") as f:
            f.write(text)  # type: ignore
