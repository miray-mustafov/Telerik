<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# Recursion In class Activity - File Utilities

The purpose of the following exercises is to practice recursion by traversing a tree-like structure (the file system)
- You are given unit tests to check the implementation of the exercise functions
- Builtin functions you are **allowed to use**:
    - `os.listdir()` - to list all files and folders in a directory
    - `os.path.join()` - to create a new path
    - `os.path.isdir()` - to check if a path is a folder
    - `os.path.split()` - to obtain a folder name
    - `os.path.splitext()` - to obtain file extension



## 1. Directory Traversal

Write a recursive function `traverse_directories(path: str) -> list[str]` which return a collection with the names of all files and folders of a given path

#### Example usage

```python
files_and_folders = traverse_directories(test_file_path)
```

#### Expected output

The test folder `demo_folder` is part of the `tests` directory. **Do not add/delete/rename anything in it.**
 - Order of elements in returned list does not matter.
```
[ 
    'demo_folder', 
    'nested-1', 
    'file-1.md', 
    'file-2.md', 
    'file-3.md',
    'nested-1-1',
    'example.txt', 
    'nested-2', 
    'test-1.csv', 
    'test-2.txt', 
    'test-3.md'
]
```

***

## 2. Find Files

Write function `find_files(path: str, extension: str) -> list[str]` which return a collection of all files which have the given `extension` in the given directory.

#### Example usage

```python
md_files = find_files(test_file_path, 'md')
txt_file = find_files(test_file_path, 'txt')
```

#### Expected output
 - Order of elements in returned lists does not matter.
```
['file-1.md', 'file-2.md', 'file-3.md', 'test-3.md']
['example.txt', 'test-2.txt']
```
***
## 3.  File Exists

Write a recursive function `file_exists(path: str, file_name: str) -> bool`. Checks whether a given file exists in the given directory and its subdirs.

#### Example usage

```python
file_exists(test_file_path, 'file-1.md')
file_exists(test_file_path, 'example.txt')
file_exists(test_file_path, 'examplee.txt')
```

#### Expected Output

```
True
True
False
```
***
## 4. Directory Stats

Write a recursive function `directory_stats(path: str) -> dict` which returns the number of files for each file extension as a dictionary of `{ str:int }`

#### Example usage

```python
directory_stats(test_file_path)
```

#### Expected Output
- Order does not matter.
```python
{'.md': 4, '.txt': 2, '.csv': 1}
```
