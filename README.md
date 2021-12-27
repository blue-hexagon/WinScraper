# WinScraper 1.0.0

A CLI tool / library used for collecting information about devices running Windows OS.

# Library

View help by importing and running WinScraper

```python
if __name__ == '__main__':
    import app.winscraper

    WinScraper()
```

Pass parameters shown in the help into the WinScraper object:

```python
if __name__ == '__main__':
    import app.winscraper

    WinScraper(cpu=True, ssid=True, software=True)
```

# CLI

View help by calling the app with the `-h` flag.

*I will create an executeable for cli-usage soon.*
```cmd
python main.py -h
```
