from setuptools import setup, Distribution
import sys


if sys.platform == "win32":
    package_data = {"pacparser": ["pacparser.dll", "_pacparser.pyd"]}

elif sys.platform == "darwin":
    package_data = {
        "pacparser": ["_pacparser.so"],
    }

else:
    raise ValueError("Not supported platform {}".format(sys.platform))


class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True


setup(
    name="pacparser",
    version="1.3.7",
    description="pacparser (PAC)",
    packages=["pacparser"],
    package_data=package_data,
    distclass=BinaryDistribution
)
