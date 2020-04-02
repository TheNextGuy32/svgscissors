from setuptools import setup, find_packages

setup(
    name = "scgScissors",
    version = "0.0.1",
    author = "Oliver Barnum",
    author_email = "oliverbarnum32@gmail.com",
    description = "Manipulate svg xml to automate data insertion.",
    url = "https://github.com/TheNextGuy32/svgScissors",
    install_requires=["asyncio", "ensure", "svgutils", "wand", "mpmath"],
    download_url="https://github.com/TheNextGuy32/svgScissors/archive/0.0.1.tar.gz",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)