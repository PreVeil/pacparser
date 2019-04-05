from setuptools import setup, Distribution


class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True


setup(
    name="pacparser",
    version="1.3.7",
    description="pacparser (PAC)",
    packages=["pacparser"],
    package_data={
        "pacparser": ["pacparser.dll", "_pacparser.pyd"],
    },
    distclass=BinaryDistribution
)
