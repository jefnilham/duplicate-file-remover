# <a href="https://jefnilham.github.io/duplicate-file-remover/" target="_blank">duplicate file remover</a>
![image](https://user-images.githubusercontent.com/39832806/155253240-c13cbc51-1fba-4082-9967-ab8eb2ada2cb.png)

Delete all duplicate files in a given folder. 

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Update](#update)

## General info
Duplicate files are a hassle to remove from our machines. I made this to help myself remove duplicates safely based on hash.

## Technologie

# Setup

# notes
- script ignores subfolders within folder and only considers files
- script compares md5 hashes of files in a folder
- any similar hashed file will be deleted, leaving first instance only

# demo
upon running, users will be asked:

![image](https://user-images.githubusercontent.com/39832806/154663786-27b0aa41-a325-45ff-8a07-d65ed6d73ed0.png)

in this example, a demo folder was created with only 2 original files, 'same content.txt' and 'different content.txt' along with their copies and other folders:

![image](https://user-images.githubusercontent.com/39832806/154663192-349dc573-5a84-4318-91ac-480408574eff.png)

after inputting chosen folder by supplying its filepath, the script will show the files it deletes as they have the same md5 hash. Note that the script will keep the first instance of the file that its hash it stores i.e. name of the original file might be different, but the contents will still be the same nonetheless:

![image](https://user-images.githubusercontent.com/39832806/154663408-54312fe9-71c7-4640-9a4d-cfc5788688b0.png)
![image](https://user-images.githubusercontent.com/39832806/154664261-c638395d-542e-4529-9eac-01089be9eb67.png)

We have removed duplicates successfully. Any further tries will show no duplicates found:

![image](https://user-images.githubusercontent.com/39832806/154663510-28013475-d235-40cf-b3dd-9d3956dd4261.png)

# UPDATE 1
- Uploaded sha256_duplicate_remover.py. Upgraded from md5 to sha256 for lesser chance of collision and deleting something wrongly.
- Added some imagery to the script


## General info
Its common to check on multiple platforms before making an online purchase. I made this for myself for items I have already purchased before (recurring purchases like coffee) as an efficient way to do a quick lookup on both platforms. I ranked the output based on popularity as I find that metric to be what I would use for this use case. On Lazada, popularity is based on ratings while on Shopee, it is based on number of items sold. Selenium was used to webscrape selected elements into resepctive lists. Pandas was used to compile all data and add a ranking system for the final output.
	
## Technologies
Project is created with:
* Webscraping with Selenium via Chrome webdriver
* Pandas for data management and display
* Variable handling
	
## Setup
Install the required modules, then run the project. I'll show my search as follows.
```
Enter item to compare: nescafe coffee 3 in 1
```
Then, wait for the ranked output as follows.
```
                                            Item Name   Price  Source  Rank
0   NESCAFE 25% Less Sugar 3in1 Instant Coffee x32...    6.15  Lazada   1.0
1   (Bundle of 3) Old Town Hazelnut 3 in 1 White C...   20.90  Shopee   1.0
2   NESCAFE Original 3 In 1 Brown Sugar 30s Instan...    6.15  Lazada   2.0
3    Killiney 3-in-1 Premium White Coffee Trio Bundle   27.93  Shopee   2.0
4   Ceo Cafe 4 In 1 3 In 1 Premix Coffee With Gano...   20.99  Shopee   3.0
5   NESCAFE 25% Less Sugar 3in1 32Sachets Instant ...    6.15  Lazada   3.5
6   (2 Pack Bundle) NESCAFE 25% Less Sugar 3in1 32...   12.00  Lazada   3.5
7   G7 ( Original - local packaging )50 sticks 3 i...  100.90  Shopee   4.0
8   NESTLE Nescafe Gold Decaf 100G X 12 (GLASS) - ...   79.90  Lazada   5.0
9   NESCAFE Blend & Brew MILD 3 in 1 Instant Coffe...    3.33  Shopee   5.0
10    Nescafe 3 in 1 Instant Coffee - Original 35x19g    9.90  Shopee   6.0
11  (2 Pack Bundle) NESCAFE Original 3in1 Brown Su...   12.00  Lazada   6.5
12        Nescafe Blend and brew original 3in1 28x19g    7.90  Lazada   6.5
13  Nescafe 3 In 1 Mild Blend & Brew Premix Coffee...   45.90  Shopee   7.0
14  (Bundle of 3) Nescafe Original Low Fat 3 in 1 ...   18.30  Shopee   8.0
15  Nescafe Blend & Brew Original – 3 in 1 Coffee ...   19.90  Shopee   9.0
16  Nescafe 3 in 1 Original 35x19g Special Promo P...   12.55  Shopee  10.0
17  NESCAFE KOPI O 2 IN 1 24 PACK X 15 STICKS X 16...   10.99  Shopee  11.0
18  [Nescafe] Decaf Coffee Decaffeinated Coffee De...    5.90  Shopee  12.0
19  [Mix and Match] Cold Brew Coffee Concentrate b...   28.80  Shopee  13.0
20  Nescafé Blend & Brew Original 3 in 1 Premix Co...   13.39  Shopee  14.0
21  Wholesales 12 Pkt/ 24 Pkt Nescafe 3 in 1 White...    8.50  Shopee  15.0
```
## Update
- Uploaded sha256_duplicate_remover.py. Upgraded from md5 to sha256 for lesser chance of collision and deleting something wrongly.
- Added some imagery to the script
