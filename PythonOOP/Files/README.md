<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# In Class Activity - Files

## Description
You are given a software system for managing files and directories. The supported functionality is:
- Creating directories/files
- Appending text to existing files
- Reading file contents
- Delete file
- Listing files in a directory
- Counting total files
- Counting total lines

## Notes
- there will be no nested directories
- you will **NOT** have to write recursive functions, no matter what the internet tries to tell you

## Task
Some of the system components are ready. You will have to finish the classes in the `commands` module

- All the directories/files will be created in the `demo_folder`.
- Search where the `NotImplemented` errors as a guide where you are expected to write code.
- You are **allowed to modify all existing code** if you need to.

### 1. Create Directory Command
- `CreateDirectory newdir`
- Creates directory with the given name
- Error message if it already exists

### 2. Create File Command
- `CreateFile newdir myfile.txt {text}`
- Creates file with the given name in the provided directory
    - creates with optional {text} or empty
- Error message if no such directory
- Error message if such a file exists in this directory

### 3. Append Text Command
- `AppendText newdir myfile.txt text`
- Appends the given text to the file in the fire
- Error message if no such file in the given directory or no such directory

### 4. Read File Command
- `ReadFile newdir myfile.txt`
- Prints all text from the given file to the console (formatted)
    - the format should start with `{file_name} contents.`
    - your command should prepend the line number to each existing file line, with 1 space of indent
    - print ` (empty)` if no content in the file
- Error message if no such file in the given directory or no such directory
- Example - `my_file.txt` - has two lines in it, `my_file2.txt` - is empty

    ```none
    my_file.txt contents:
     1. this is some content
     2. this is another line

    my_file2.txt contents:
     (empty)
    ```

### 5. Delete File Command
- `DeleteFile newdir myfile.txt`
- Deletes the file in this directory
- Error message if no such file in the given directory or no such directory

### 6. List Files Command
- `ListsFiles newdir`
- Lists all files in the given directory, each file name on a new line, along with a line number
- Error message if no such directory
- Output example:
    ```none
    newdir files:
     1. my_file.txt
     2. my_file2.txt

    anotherdir files:
     (empty)
    ```

### 7. Count Files Command
- `CountFiles`
- Counts all files in the `demo_folder`
- Output: `Total files in demo_folder: {count}`

### 8. Count Lines Command
- `CountLines`
- Counts all lines in all txt files in the `demo_folder`
- Output: `Total lines in all files in demo_folder: {count}`

***

### Input
```none
CreateDirectory newdir
CreateDirectory newdir
CreateFile newdir my_file.txt this is some content
CreateFile newdir my_file2.txt
CreateFile newdir my_file2.txt
AppendText newdir my_file.txt this is another line
ReadFile newdir my_file.txt
ReadFile newdir my_file2.txt
DeleteFile newdir my_file2.txt
CreateDirectory anotherdir
ListFiles newdir
ListFiles anotherdir
ListFiles nosuchdir 
CreateFile anotherdir my_file.txt file content
AppendText anotherdir my_file.txt this is another line
AppendText anotherdir my_file.txt this is another line
AppendText anotherdir my_file.txt this is another line
CountFiles
CountLines
Exit
```
If you run the program with the same input more than once, the output should be different.

### Output
```none
Directory newdir created.
Directory newdir already exists.
File my_file.txt created.
File my_file2.txt created.
File my_file2.txt already exists.
New line appended to file my_file.txt.
my_file.txt contents:
 1. this is some content
 2. this is another line
my_file2.txt contents:
 (empty)
File my_file2.txt deleted.
Directory anotherdir created.
newdir files:
 1. my_file.txt
anotherdir files:
 (empty)
Directory nosuchdir does not exist.
File my_file.txt created.
New line appended to file my_file.txt.
New line appended to file my_file.txt.
New line appended to file my_file.txt.
Total files in demo_folder: 2
Total lines in all files in demo_folder: 6
```
