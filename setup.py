import pathlib

from setuptools import find_packages, setup

VERSION = "1.0.8"
NAME = "winscraper"
DESCRIPTION = "A CLI tool and a library used for collecting information about devices running the Windows OS."
WORKING_DIR = pathlib.Path(__file__).parent
README_CONTENT = (WORKING_DIR / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    author="Manjana",
    author_email="w0j8uhv5csio@opayq.net",
    description=DESCRIPTION,
    long_description=README_CONTENT,
    long_description_content_type="text/markdown",
    # options={"bdist_wheel": {"universal": True}},
    url="https://www.github.com/blue-hexagon/winscraper",
    project_urls={
        "Bug Tracker": "https://github.com/blue-hexagon/winscraper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "Topic :: Security",
        "Topic :: System :: Monitoring",
        "Development Status :: 5 - Production/Stable",
    ],
    keywords="system monitoring monitor",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    include_package_data=True,
    install_requires=["psutil==5.8.0", "pywinauto==0.6.8", "pywin32==303", "wmi==1.5.1"],
    entry_points={
        "console_scripts": [
            "winscraper=winscraper:main",
        ]
    },
)
