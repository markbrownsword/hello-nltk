from setuptools import setup

setup(
    name = 'helloNLTK',
    version = '0.1.0',
    packages = ['helloNLTK'],
    entry_points = {
        'console_scripts': [
            'helloNLTK = helloNLTK.__main__:main'
        ]
    },
    install_requires=['nltk'])
