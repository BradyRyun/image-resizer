from setuptools import setup, find_packages

setup(
    name="image-resizer", 
    version="0.1.0",
    author="Brady Ryun",
    author_email="brady@ryunengineering.com",
    description="Resizes images in a directory or any specific image.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="http://github.com/bradyryun/image-resizer", 
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11.3",
    ],
    include_package_data=True,
)
