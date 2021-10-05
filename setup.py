from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Life remainder'
LONG_DESCRIPTION = 'Python module that creates a file to remind you how quickly time pass'

setup(
    name="weeksOfLife",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Diac Adrian",
    author_email="diacadi@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=['pillow'],
    keywords=['image','pyhton','png','week','life'],
    classifiers= [
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)