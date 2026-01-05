import os
import pathlib
import pkg_resources
from setuptools import setup, find_packages


PKG_NAME = "waypoint_extraction"
VERSION = "0.1"
EXTRAS = {}


def _read_file(fname):
    # this_dir = os.path.abspath(os.path.dirname(__file__))
    # with open(os.path.join(this_dir, fname)) as f:
    with pathlib.Path(fname).open() as fp:
        return fp.read()


def _read_install_requires():
    # Use __file__ to get correct path regardless of cwd
    this_dir = pathlib.Path(__file__).parent
    req_path = this_dir / "requirements.txt"
    with req_path.open() as fp:
        reqs = [
            str(requirement) for requirement in pkg_resources.parse_requirements(fp)
        ]
    # Exclude mujoco-py (not needed for robosuite 1.5+ with mujoco 3.x)
    reqs = [r for r in reqs if not r.startswith("mujoco-py")]
    return reqs


def _fill_extras(extras):
    if extras:
        extras["all"] = list(set([item for group in extras.values() for item in group]))
    return extras


setup(
    name=PKG_NAME,
    version=VERSION,
    author=f"IRIS",
    url="",
    description="research project",
    long_description=_read_file("README.md"),
    long_description_content_type="text/markdown",
    keywords=["Deep Learning", "Machine Learning"],
    license="MIT License",
    packages=find_packages(include=f"{PKG_NAME}.*"),
    include_package_data=True,
    zip_safe=False,
    install_requires=_read_install_requires(),
    extras_require=_fill_extras(EXTRAS),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Environment :: Console",
        "Programming Language :: Python :: 3.9",
    ],
)
