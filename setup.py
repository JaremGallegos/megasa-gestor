from setuptools import find_packages, setup
    
setup(
    name = "gestionar-publicidad",
    version = "0.1.0",
    description = "Un proyecto para poder gestionar clientes de una empresa eCommerce",
    package_dir = {"": "src"},
    packages = find_packages(where = "src"),
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/JaremGallegos/gestionar-clientes-python.git",
    author = "JaremGallegos",
    author_email = "73142526@continental.edu.pe",
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12.4",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        ""
    ],
    python_requires = ">= 3.12.4"
)