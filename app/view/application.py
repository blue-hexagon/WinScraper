import json
import logging
import sys
from typing import Any, Dict, List

from app.helper.assistant import TextFileSaver
from app.helper.descriptor_helper import Descriptors
from app.view.help import HelpView


class ApplicationView:
    def __init__(self, **kwargs: Dict[str, bool] | bool) -> None:
        self.bucket: List[Any] = []
        descriptors = Descriptors

        for descriptor in descriptors.get_all_descriptors():
            try:
                if kwargs[descriptor.parameter] or kwargs[descriptor.category.parameter] or kwargs["all"]:
                    self.bucket.append(descriptor.collector())
            except KeyError:
                continue
        if len(self.bucket) == 0:
            HelpView.display()
            logging.getLogger().error(
                "No collector selected. You must select at least one selector.\n"
                "If running from the CLI, use the -h flag for help."
            )
            sys.exit(1)
        self.collection = []
        for collector in self.bucket:
            self.collection.append(collector.collect())

    def save(self) -> None:
        TextFileSaver.save_as_text(*self.collection)

    def print(self) -> None:
        print(json.dumps(self.collection, indent=2, ensure_ascii=True))
