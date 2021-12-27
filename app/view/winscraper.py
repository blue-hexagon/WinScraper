import json
import sys
from typing import Any, Dict, List

from app.helper.assistant import TextFileSaver
from app.helper.descriptor_helper import Descriptors


class WinScraper:
    def __init__(self, **kwargs: Dict[str, bool]) -> None:
        self.bucket: List[Any] = []
        descriptors = Descriptors

        for descriptor in descriptors.get_all_descriptors():
            if kwargs[descriptor.parameter] or kwargs[descriptor.category.parameter] or kwargs["all"]:
                self.bucket.append(descriptor.collector())
        if len(self.bucket) == 0:
            sys.exit("No collector selected. You must set at least one named parameter to True.")
        self.collection = []
        for collector in self.bucket:
            self.collection.append(collector.collect())

    def save(self) -> None:
        TextFileSaver.save_as_text(*self.collection)

    def print(self) -> None:
        print(json.dumps(self.collection, indent=2, ensure_ascii=True))
