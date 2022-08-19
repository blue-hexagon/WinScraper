# WinScraper 1.0.0

A CLI tool / library used for collecting information about devices running Windows OS.

# Getting Started
```python
git clone https://github.com/blue-hexagon/WinScraper.git
pip install -r requirements.txt
```

# Compiling to Binary

1. `auto-py-to-exe.exe --no-ui -c .\resources\auto-py-to-exe-config.json -o .\output\`
2. Open the link in the terminal
3. Click CONVERT .PY TO .EXE
4. Run the application from a terminal: `./output/winscraper.exe`
# Using as a Library

View help by importing and running WinScraper

```python
if __name__ == '__main__':
    from src.main import WinScraper

    WinScraper()
```

Pass parameters shown in the help into the WinScraper object:

```python
if __name__ == '__main__':
    from src.main import WinScraper

    WinScraper(cpu=True, ssid=True, software=True)
```

# Using as a CLI

View a detailed options list by calling the app with the `-h` flag.
```text
(venv) PS C:\Users\username\Desktop\winscraper> python .\winscraper.py -h
usage: Collect a plethora of information about this device and everything related to it. [-h] [--system] [--cpu] [--ram] [--harddrive] [--interface] [--ssid] [--startup-software] [--installed-software] [--pid] [--all] [--hardware] [--network]
                                                                                         [--process] [--software] [--uncategorized]

options:
  -h, --help            show this help message and exit
  --system              Collect device and system information
  --cpu                 Gathers information about the CPU such as the number of cores and their utilization
  --ram                 Collects information about the devices RAM consumption and resources
  --harddrive           Collects information about disks and partitions as well as their usage
  --interface           Collects information about the devices network adapters, assigned IP addresses, MAC addresses and more
  --ssid                Collects saved SSID and their associated passwords if such exists
  --startup-software    Scan the windows registry for software which is executed at startup
  --installed-software  Scan the windows registry for installed software
  --pid                 Collects all process names and IDs
  --all                 All modules (everything)
  --hardware            All hardware modules
  --network             All network modules
  --process             All process modules
  --software            All software modules
  --uncategorized       All uncategorized modules
```

Or invoke the default HelpView: `python winscraper.py` which displays how CLI args maps to object arguments.
```text
(venv) PS C:\Users\zbctobia\Desktop\winscraper> python .\winscraper.py
#   Collector                     Shell Long Option     Instance Parameter
---------------------------------------------------------------------------
1.  Everything                    --all                 all=True

2.  Hardware                      --hardware            hardware=True
2.1 CPU Collector                 --cpu                 cpu=True
2.2 RAM Collector                 --ram                 ram=True
2.3 Harddrive Collector           --harddrive           harddrive=True

3.  Network                       --network             network=True
3.1 Network Interface Collector   --interface           interface=True
3.2 SSID Collector                --ssid                ssid=True

4.  Process                       --process             process=True
4.1 Process ID Collector          --pid                 pid=True

5.  Software                      --software            software=True
5.1 Startup Software Collector    --startup-software    startup_software=True
5.2 Installed Software Collector  --installed-software  installed_software=True

6.  Uncategorized                 --uncategorized       uncategorized=True
6.1 System Information Collector  --system              system=True

No collector selected. You must select at least one selector.
If running from the CLI, use the -h flag for help.

```

## Contributing
For new features raise an issue and wait for permission

For fixes make a pull request.

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/blue-hexagon/winscraper/tags).

## Authors
- **Manjana** - *Initial work* - [manjana](https://github.com/blue-hexagon)

See also the list of [contributors](https://github.com/blue-hexagon/winscraper/contributors) who participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
