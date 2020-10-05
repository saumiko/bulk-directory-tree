
# Bulk Directory Tree  
[![Build Status](https://travis-ci.org/saumiko/bulk-directory-tree.svg?branch=master)](https://travis-ci.org/saumiko/bulk-directory-tree)
[![Requirements Status](https://requires.io/github/saumiko/bulk-directory-tree/requirements.svg?branch=master)](https://requires.io/github/saumiko/bulk-directory-tree/requirements/?branch=master)
[![PyPI](https://img.shields.io/pypi/v/bulk-directory-tree.svg)](https://pypi.org/project/bulk-directory-tree)
[![star this repo](https://img.shields.io/github/stars/saumiko/bulk-directory-tree)](https://github.com/saumiko/bulk-directory-tree) 
[![fork this repo](https://img.shields.io/github/forks/saumiko/bulk-directory-tree)](https://github.com/saumiko/bulk-directory-tree/fork)  
  
Creates `n` number of directories for `d` depth at any directory.  
  
- [Installation](#installation)  
- [Description](#description)  
- [Options](#options)  
- [Defaults](#defaults)  
- [Example](#example)  
  
## Installation  
You can use pip to install this command line tool:  
  
```sudo -H pip install --upgrade bulk-directory-tree```  
  
## Description  
`bulk-directory-tree` is a command-line program to create `n` number of directories for `d` depth at given directory. It requires the Python interpreter, version 2.6, 2.7, or 3.2+, and it is not platform specific. It should work on your Unix box, on Windows or on macOS. It is released to the public domain, which means you can modify it, redistribute it or use it however you like.  
  
```  
bulk-directory-tree [OPTIONS]  
```  
## Options  
```  
-p, --path TEXT Bulk Directory Creation Path  
-n, --num INTEGER Number of folders to create in each directory  
-d, --depth INTEGER Directory tree depth  
-l, --length INTEGER  Directory name length  
--help  Show this message and exit.  
```  
  
## Defaults  
```  
-p, --path        YOUR_CURRENT_DIRECTORY  
-n, --num     1  
-d, --depth       1  
-l, --length   5  
```  
  
## Example  
`$ bulk-directory-tree -p '$YOUR_DIRECTORY' -n 3 -d 3 -l 4`  
  
Running this command will create a directory tree like shown below in `YOUR_DIRECTORY`  
  
```  
YOUR_DIRECTORY
├── 0c6c
│   ├── 1036
│   │   ├── 65b3
│   │   ├── 79c2
│   │   └── 7dca
│   ├── 575d
│   │   ├── 3097
│   │   ├── 6526
│   │   └── 8567
│   └── fc27
│       ├── 50b8
│       ├── 53ad
│       └── 650e
├── 5d16
│   ├── 8880
│   │   ├── 12c7
│   │   ├── 63d4
│   │   └── 701a
│   ├── b846
│   │   ├── 6f2c
│   │   ├── 761b
│   │   └── 8ebd
│   └── ba2d
│       ├── 75da
│       ├── 8405
│       └── ccb1
└── fc02
    ├── 53b8
    │   ├── 06d8
    │   ├── 73d0
    │   └── 9bf7
    ├── 8406
    │   ├── 37d9
    │   ├── 6954
    │   └── d3d4
    └── ec6f
        ├── 7150
        ├── 9d9f
        └── b846
```