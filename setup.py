from setuptools import setup, find_packages

setup(
    name='ezqc',
    version='0.1',
    author='Tinger Shi & Sky Li',
    description='EZQC is a streamlined, terminal-based alternative to FastQC.',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
        'numpy',
        'matplotlib',
        'pandas',
        'scipy',
        'Bio',
    ],
    entry_points={
        'console_scripts': [
            'ezqc=ezqc.ezqc:main',
        ],
    },
)
