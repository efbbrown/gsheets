import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ggsheets-efbbrown",
    version="0.0.1",
    author="Eugene Brown",
    author_email="efbbrown@gmail.com",
    description="A package to download from and upload to google sheets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/efbbrown/gsheets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
