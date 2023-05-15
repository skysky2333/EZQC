from setuptools import setup, find_packages

setup(
    name='ezqc',
    version='1.0',
    author='Tinger Shi & Sky Li',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'ezqc=ezqc.ezqc:main',
        ],
    },
)
