import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ropython",  # Replace with your own username
    version="0.1.0",
    author="parker02311",
    author_email="parker02311contact@gmail.com",
    description="A API wrapper for interacting with developer products in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/parker02311/Custom-Developer-Products-Python/tree/master",
    packages=["ropython"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)
