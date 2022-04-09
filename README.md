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
Save the raw code and run the python script.
```
Enter filepath to sort folder by file type:
```

In this demo setup, a demo folder was created with only 2 original files, 'same content.txt' and 'different content.txt' along with their copies and other folders:

![image](https://user-images.githubusercontent.com/39832806/154663192-349dc573-5a84-4318-91ac-480408574eff.png)

After inputting chosen folder by supplying its filepath, the script will show the files it deletes as they have the same md5 hash. Note that the script will keep the first instance of the file that its hash it stores i.e. name of the original file might be different, but the contents will still be the same nonetheless:

![image](https://user-images.githubusercontent.com/39832806/154663408-54312fe9-71c7-4640-9a4d-cfc5788688b0.png)
![image](https://user-images.githubusercontent.com/39832806/154664261-c638395d-542e-4529-9eac-01089be9eb67.png)

We have removed duplicates successfully. Any further tries will show no duplicates found:

![image](https://user-images.githubusercontent.com/39832806/154663510-28013475-d235-40cf-b3dd-9d3956dd4261.png)


## Update
- Uploaded sha256_duplicate_remover.py. Upgraded from md5 to sha256 for lesser chance of collision and deleting something wrongly.
- Added some imagery to the script
