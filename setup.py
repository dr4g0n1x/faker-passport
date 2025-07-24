from setuptools import setup, find_packages

# Read the README file if it exists
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A Faker provider for generating passport data"

setup(
    name="faker-passport-custom",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Faker provider for generating passport data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/faker-passport",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "faker>=8.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.10.0",
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ]
    },
)
