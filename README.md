# WinScraper 1.0.0

A CLI tool / library used for collecting information about devices running Windows OS.

# Getting Started
```python
pip install winscraper
```
```python
git clone ...
pip install -r requirements.txt
```
# Using as a Library

View help by importing and running WinScraper

```python
if __name__ == '__main__':
    import src.winscraper

    WinScraper()
```

Pass parameters shown in the help into the WinScraper object:

```python
if __name__ == '__main__':
    import src.winscraper

    WinScraper(cpu=True, ssid=True, software=True)
```

# Using as a CLI

View help by calling the app with the `-h` flag.

*I will create an executeable for cli-usage soon.*
```cmd
python main.py -h
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
