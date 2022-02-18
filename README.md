# duplicate-remover
Script to delete any duplicate files in a given folder. 

# notes
- script ignores subfolders within folder and only considers files
- script compares md5 hashes of files in a folder
- any similar hashed file will be deleted, leaving first instance only

# demo
upon running, users will be asked:

![image](https://user-images.githubusercontent.com/39832806/154663786-27b0aa41-a325-45ff-8a07-d65ed6d73ed0.png)

in this example, a demo folder was created with only 2 original files, 'same content.txt' and 'different content.txt' along with their copies and other folders:

![image](https://user-images.githubusercontent.com/39832806/154663192-349dc573-5a84-4318-91ac-480408574eff.png)

after inputting chosen folder by supplying its filepath, the script will show the files it deletes as they have the same md5 hash. Note that the script will keep the first instance of the file that its hash it stores. This means that the script will kepe only that first file that it comes across i.e. name of the original file might be different, but the contents will still be the same nonetheless:

![image](https://user-images.githubusercontent.com/39832806/154663408-54312fe9-71c7-4640-9a4d-cfc5788688b0.png)
![image](https://user-images.githubusercontent.com/39832806/154664261-c638395d-542e-4529-9eac-01089be9eb67.png)


We have removed duplicates successfully. Any further tries will show no duplicates found:

![image](https://user-images.githubusercontent.com/39832806/154663510-28013475-d235-40cf-b3dd-9d3956dd4261.png)

