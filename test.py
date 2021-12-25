import wmi

if __name__ == "__main__":
    if True:
        c = wmi.WMI()
        # for s in c.Win32_StartupCommand():
        #     print("[%s] %s <%s>" % (s.Location, s.Caption, s.Command))
        for share in c.Win32_Share():
            print(share.Name, share.Path)
