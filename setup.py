from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='bulk_directory_tree',
    version='0.0.7',
    py_modules=['bulk_directory_tree.py'],
    install_requires=[
        'Click==7.0'
    ],
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    entry_points='''
        [console_scripts]
        bulk-directory-tree=bulk_directory_tree:main
    ''',
    author="Asif Mohaimen",
    author_email="saumik01@gmail.com",
    description="Create n node d depth bulk directory tree in any directory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saumiko/bulk-directory-tree",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
