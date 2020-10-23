from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requires = f.read().splitlines()

setup(
    name="baricadr",
    version='0.0.1',
    description="Baricadr library",
    author="Mateo Boudet",
    author_email="mateo.boudet@inrae.fr",
    url="https://github.com/baricadr/baricadr_cli",
    install_requires=requires,
    packages=find_packages(),
    license='MIT',
    platforms="Posix; MacOS X; Windows",
    entry_points='''
        [console_scripts]
        barique=barique.cli:barique
    '''
    )
