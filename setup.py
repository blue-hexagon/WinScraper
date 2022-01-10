import pathlib

from setuptools import find_packages, setup

VERSION = "1.0.0"
NAME = "winscraper"
DESCRIPTION = "A CLI tool and a library used for collecting information about devices running the Windows OS."
WORKING_DIR = pathlib.Path(__file__).parent
README_CONTENT = (WORKING_DIR / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    scripts=["./src/app/winscraper.py"],
    author="Manjana",
    author_email="w0j8uhv5csio@opayq.net",
    description=DESCRIPTION,
    long_description=README_CONTENT,
    long_description_content_type="text/markdown",
    options={"bdist_wheel": {"universal": True}},
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
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    # py_modules=[""],
    # include_package_data=True,
    install_requires=["psutil", "wmi", "pywinauto"],
    # entry_points={
    #    "console_scripts": [
    #        "winscraper=app.winscraper.__main__:main",
    #    ]
    # },
)
