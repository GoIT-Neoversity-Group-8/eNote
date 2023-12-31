from setuptools import setup, find_namespace_packages

setup(
    name="eNote",
    version="0.1",
    author="Transcarpathian Raccoon",
    url="https://github.com/GoIT-Neoversity-Group-8/eNote",
    packages=find_namespace_packages(),
    install_requires=["tabulate", "prompt_toolkit", "colorama"],
    entry_points={
        "console_scripts": [
            "enote = eNote.app.command_bot:address_book_bot",
        ],
    },
)
