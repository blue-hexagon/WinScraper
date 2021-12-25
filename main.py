from app.winscraper import SimpleDiner

if __name__ == "__main__":
    if False:
        sys = SimpleDiner.help()

    else:
        sysinfo = SimpleDiner(
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
