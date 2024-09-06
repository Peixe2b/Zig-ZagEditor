from setuptools import setup
from zigzag import VERSION


setup(
    name='Zig/ZagEditor',
    version=VERSION,
    packages=['my_project'],
    entry_points={
        'console_scripts': [
           'my_project = my_project.cli:main',
        ],
    },
    install_requires=[
        'colordorama',
        'docopt',
    ],
    author='Peixe2b',
    author_email='jclodoaldosantana204@gmail.com',
    description='A text editor similar to Vim for editing text files. For new programmers.',
    long_description="A lightweight and powerful editor to help programmers and writers create text quickly and efficiently.",
    long_description_content_type='text/markdown',
    url='https://github.com/Peixe2b/Zig-ZagEditro',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
