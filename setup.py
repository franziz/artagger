from setuptools import setup

setup(
    name='artagger',
    version='0.1.2',
    description='RDRPOSTagger Implementation.',
    author='Frans Huang',
    author_email='franssiswanto@gmail.com',
    url='https://github.com/franziz/artagger/',
    packages=["artagger", "artagger.InitialTagger", "artagger.SCRDRlearner", "artagger.Utility"],
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
    ],
)