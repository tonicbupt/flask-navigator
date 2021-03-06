from setuptools import setup, find_packages
from os.path import dirname, realpath, join


def read_long_description():
    current_dir = dirname(realpath(__file__))
    with open(join(current_dir, "README.md")) as long_description_file:
        return long_description_file.read()


setup(
    name="Flask-Navigator",
    packages=find_packages(exclude=["tests", "docs"]),
    version='0.1.0',
    description="The navigation of Flask application.",
    long_description=read_long_description(),
    author="Jiangge Zhang, Modifier:tonic",
    author_email="tonyseek@gmail.com",
    url="http://code.dapps.douban.com/flask-navigator",
    license="MIT",
    keywords=["navigator", "flask", "navbar", "nav"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=["Flask", "blinker"],
)
