import json
import logging
import sys
from typing import Any, Dict, List

import yaml  # type: ignore

from src.helper.assistant import TextFileSaver
from src.helper.descriptor_helper import Descriptors
from src.view.help import HelpView


class ApplicationView:
    def __init__(self, formatting: str, **kwargs: Dict[str, bool] | bool) -> None:
        self.bucket: List[Any] = []
        self.formatting = formatting.lower()  # 'JSON' or 'YAML'
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
        json_data = json.dumps(self.collection, indent=2, ensure_ascii=True)
        if self.formatting == "json":
            print(json_data)
        elif self.formatting == "yaml":
            print(yaml.dump(yaml.safe_load(json_data)))
