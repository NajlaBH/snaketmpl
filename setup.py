#****
# Created by NajlaBH
# Feb 21
#****

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snaketmpl", # Replace with your own username
    version="0.1.0",
    author="NajlaBH",
    author_email="bhndevtools@gmail.com",
    description="A template for snakemake workflow.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Najlabioinfo/snaketmpl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)