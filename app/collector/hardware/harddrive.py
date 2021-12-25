from typing import Any, Dict

import psutil

from app.app_assister import ByteUnitConverter
from app.collector.base_collector import BaseCollector
from app.collector.collection_category import CollectionCategory


class DiskCollector(BaseCollector):
    def __init__(self) -> None:
        super().__init__(
            name="Harddrive Collector",
            description="Collects information about disks and partitions as well as their usage",
            category=CollectionCategory.HARDWARE,
            cmd_arg="--disk",
        )

    def collect(self) -> Dict[Any, Any]:
        disk_io = psutil.disk_io_counters()  # get IO statistics since boot
        partitions = psutil.disk_partitions()  # get all disk partitions
        partition_list = {}
        for partition in partitions:
            partition_list[partition.device] = {
                "Mountpoint": partition.mountpoint,
                "Filesystem": partition.fstype,
            }
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:  # this can be caught due to the disk that isn't ready
                continue
            partition_list[partition.device]["Total Size"] = ByteUnitConverter.get_size(partition_usage.total)
            partition_list[partition.device]["Used"] = ByteUnitConverter.get_size(partition_usage.used)
            partition_list[partition.device]["Free"] = ByteUnitConverter.get_size(partition_usage.free)
            partition_list[partition.device]["Percentage"] = f"{partition_usage.percent}%"

        self.json_output.setdefault(
            "Disk Information",
            {
                "Total Read": ByteUnitConverter.get_size(disk_io.read_bytes),
                "Total Write": ByteUnitConverter.get_size(disk_io.write_bytes),
                "Partitions": partition_list,
            },
        )
        return self.json_output