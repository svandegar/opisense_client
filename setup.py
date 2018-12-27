import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opisense_client",
    version="0.2.0",
    author="Seraphin Vandegar",
    author_email="svandegar@hotmail.com",
    description="Package to interact with the Opisense API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/opinum/opisense_client/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)