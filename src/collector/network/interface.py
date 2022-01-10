from typing import Any, Dict

import psutil

from src.collector.base_collector import BaseCollector
from src.helper.assistant import ByteUnitConverter


class InterfaceCollector(BaseCollector):
    def __init__(self) -> None:
        super().__init__()

    def collect(self) -> Dict[Any, Any]:
        if_addrs = psutil.net_if_addrs()  # Get all network interfaces (virtual and physical)
        net_io = psutil.net_io_counters()  # Get IO statistics since boot
        if_dict_enumerator: Dict[Any, Any] = {}
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                # NOTE: On Linux there is another address family: .AF_PACKET
                if str(address.family) == "AddressFamily.AF_INET":
                    try:
                        if_dict_enumerator[interface_name].update(
                            {
                                "IP Address": address.address,
                                "Netmask": address.netmask,
                                "Broadcast IP": address.broadcast,
                            }
                        )
                    except KeyError:
                        if_dict_enumerator[interface_name] = {
                            "IP Address": address.address,
                            "Netmask": address.netmask,
                            "Broadcast IP": address.broadcast,
                        }
                elif str(address.family) == "AddressFamily.AF_INET6":
                    try:
                        if_dict_enumerator[interface_name].update(
                            {
                                "Link-Local IPv6 Address"
                                if address.address.startswith("fe80")
                                else "IPv6 Address": address.address,
                            }
                        )
                    except KeyError:
                        if_dict_enumerator[interface_name] = {
                            "Link-Local Address"
                            if address.address.startswith("fe80")
                            else "IPv6 Address": address.address,
                        }
                elif str(address.family) == "AddressFamily.AF_LINK":
                    try:
                        if_dict_enumerator[interface_name].update(
                            {
                                "MAC": address.address,
                            }
                        )
                    except KeyError:
                        if_dict_enumerator[interface_name] = {
                            "MAC": address.address,
                        }
        self.json_output.setdefault(
            "Network Information",
            {
                "Total Bytes Sent": ByteUnitConverter.get_size(net_io.bytes_sent),
                "Total Bytes Received": ByteUnitConverter.get_size(net_io.bytes_recv),
                "Interfaces": if_dict_enumerator,
            },
        )
        return self.json_output
