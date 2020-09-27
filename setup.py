from setuptools import setup, find_packages


with open("README.md") as _file:
    readme = _file.read()

with open("LICENSE") as _file:
    license = _file.read()

setup(
    name = "Clicker Keyse",
    version= "0.0.1",
    description="Keyboard and mouse action recorder.",
    long_description=readme,
    author="Lupauloz",
    author_email="luizpaulo1290@live.com",
    url="https://github.com/LuPauloz/Clicker-Keyse",
    license=license

)