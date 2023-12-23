from setuptools import setup, find_packages

setup(
    name="eNote",
    version="0.1",
    author="Transcarpathian Raccoon",
    url="https://github.com/GoIT-Neoversity-Group-8/eNote",
    package_dir={"": "eNote"},
    packages=find_packages(where="eNote"),
    install_requires=["tabulate", "prompt_toolkit"],
    entry_points={
        "console_scripts": [
            "enote = app.command_bot:address_book_bot",
        ],
    },
)
