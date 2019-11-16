from os import path

from setuptools import setup

# Read the contents of README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="artagger",
    version="0.1.3",
    description="A Ripple Down Rules-based (RDR) Part-Of-Speech Tagger implementation based on RDRPOSTagger.",
    # other arguments omitted
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Frans Huang",
    author_email="franssiswanto@gmail.com",
    url="https://github.com/franziz/artagger/",
    packages=[
        "artagger",
        "artagger.InitialTagger",
        "artagger.SCRDRlearner",
        "artagger.Utility",
    ],
    include_package_data=True,
    license="MIT",  # Or Apache License 2.0 as stated in GitHub?
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: Thai",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Linguistic",
    ],
)
