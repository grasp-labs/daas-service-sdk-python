from glob import glob
from os.path import basename
from os.path import splitext
from setuptools import setup, find_packages


__VERSION__ = "0.0.5"

setup(
    name="daas-service-sdk",
    version=__VERSION__,
    description="Daas Service SDK for Python",
    url="https://github.com/grasp-labs/daas-service-sdk-python",
    author="Grasp Labs",
    author_email="yuan@grasplabs.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="daas service sdk python",
    python_requires=">=3.7",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("daas_service_sdk/*.py")],
    include_package_data=True,
    install_requires=["requests"],
    project_urls={
        "Issue Tracker": "https://github.com/grasp-labs/daas-service-sdk-python/issues",
    },
)
