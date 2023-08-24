import os
from glob import glob

from setuptools import find_packages, setup

package_name = "ipb_car_launch"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/" + package_name, ["package.xml"]),
        # Install launch XML files
        (
            os.path.join("share", package_name, "launch"),
            glob(os.path.join("launch", "*launch.[pxy][yma]*")),
        ),
        # Install config files
        (
            os.path.join("share", package_name, "config"),
            glob(os.path.join("config", "**/*.yaml")),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="ivizzo",
    maintainer_email="ivizzo@uni-bonn.de",
    description="ipb-car launch files",
    license="MIT",
)
