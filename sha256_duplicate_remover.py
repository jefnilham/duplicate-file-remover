import os
import hashlib

# give folder to clear duplicate files
print(
"""
___        __         __  __  ___  __
|  | |  | |__| |   | |   |__|  |  |_
|  | |  | |    |   | |   |  |  |  |
|_/  |__| |    |__ | |__ |  |  |  |__

R     E     M     O     V     E     R

""")

print("Enter filepath to remove any duplicates within: ")

folder_to_check = input("")

# change dir
os.chdir(folder_to_check)
folder_to_check_contents = os.listdir(folder_to_check)

# get sha256 hash function. 
# check for file binary, name can be different but as long content is same, it will be found
# # Name must always be different in a folder anyway
def file_sha256(file):
    sha256_hash = hashlib.sha256()
    with open(file, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# counting initial number of files
count = 0
for file in folder_to_check_contents:
    if os.path.isdir(file) == False:
        count += 1

# init list to collect all hashes to compare with
sha256_list = []

# looks through given folder and automatically deletes duplicates, leaving only first instance untouched
for file in folder_to_check_contents:
    if os.path.isdir(file) == False:
        filehash = file_sha256(file)
        if filehash in sha256_list:
            os.remove(file)
            print('Removing duplicates:', file)
        else:
            sha256_list.append(filehash)

# count file difference
file_count_difference = count - len(sha256_list)

# closing statement
if file_count_difference == 0:
    print("No duplicates found in", folder_to_check)
elif file_count_difference == 1:
    print(file_count_difference, 'file duplicate deleted in', folder_to_check)
else:
    print(file_count_difference, 'file duplicates deleted in', folder_to_check)
