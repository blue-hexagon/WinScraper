from typing import Any, Dict

import wmi

from app.collector.base_collector import BaseCollector
from app.collector.collection_category import CollectionCategory


class StartupProgramsCollector(BaseCollector):
    def __init__(self) -> None:
        super().__init__(
            name="Startup Software Collector",
            description="...",
            category=CollectionCategory.SOFTWARE,
            cmd_arg="--startup-software",
        )
        self.c = wmi.WMI()

    def collect(self) -> Dict[Any, Any]:
        items: Dict[Any, Any] = {}
        for s in self.c.Win32_StartupCommand():
            items.setdefault(
                s.Caption,
                {
                    "Name": s.Name,
                    "Description": s.Description,
                    "User": s.User,
                    "UserSID": s.UserSID,
                    "SettingID": s.SettingID,
                    "Location": s.Location,
                    "Command": s.Command,
                },
            )
        return {"Startup Programs": items}
