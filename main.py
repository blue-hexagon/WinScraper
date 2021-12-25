from app.winscraper import Diner

if __name__ == "__main__":
    if True:
        Diner(network=True).print()

    else:
        sysinfo = Diner(
            network_interfaces=True,
            cpu_information=True,
            memory_information=True,
            disk_information=True,
            system_information=True,
            ssid_password_lister=True,
            get_startup_programs=True,
            running_processes=True,
            installed_software=True,
        )
        sysinfo.print()
