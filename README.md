# <a href="https://jefnilham.github.io/duplicate-file-remover/" target="_blank">duplicate file remover</a>
![image](https://user-images.githubusercontent.com/39832806/155253240-c13cbc51-1fba-4082-9967-ab8eb2ada2cb.png)

Delete all duplicate files in a given folder. 

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Update](#update)

# General info
It is difficult to remove existing duplicates in a folder, especially on machines which have been around longer where folders tend to get bloated with files. I made this to automate the task of removing duplicates safely based on file hash. The user inputs the chosen folder and the script iterates through and check for files, ignoring subfolders. The hash function is run for every file and each file hash is stored in a list. Therefore, the script looks through the folder and removes anything that is not the first stored hash instance i.e. any second or more instances of the file is removed.

## Technologies
- Hashlib to generate file hashes. Chosen algorithms are MD5 and SHA256
- Miscellaneous operating system interfaces for directory traverals and file deletions

## Setup
Save the raw code and run the python script. The following is a demo setup with this folder prepared:
```
Enter filepath to sort folder by file type: C:\Users\Music\test_desktop
```

In this demo setup, a demo folder was created with only 2 original files, 'same content.txt' and 'different content.txt' along with their copies and other folders:

![image](https://user-images.githubusercontent.com/39832806/162561447-3d3105fd-8a55-4ced-b060-d75c594a17bc.png)

After inputting chosen folder by supplying its filepath, the script will show the files it deletes as they have the same md5 hash. Note that the script will keep the first instance of the file that its hash it stores i.e. name of the original file might be different, but the contents will still be the same nonetheless:
```
Enter filepath to sort folder by file type:C:\Users\Music\test_desktop
Removing duplicates: different content - Copy.txt
Removing duplicates: different content.txt
Removing duplicates: same content.txt
3 file duplicates deleted in C:\Users\Music\test_desktop
```
![image](https://user-images.githubusercontent.com/39832806/162561431-1ecd0201-0aa1-4402-93ed-308c879a0dd1.png)

We have removed duplicates successfully. Any further tries on that same folder will show no duplicates found:
```
Enter filepath to sort folder by file type:C:\Users\Music\test_desktop
No duplicates found in C:\Users\Music\test_desktop
```


## Update
- Uploaded sha256_duplicate_remover.py. Upgraded from md5 to sha256 for lesser chance of collision and deleting something wrongly.
- Added some imagery to the script
