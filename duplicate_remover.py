import os
import hashlib

# give folder to clear duplicate files
folder_to_check = input("Enter filepath to sort folder by file type:")

# change dir
os.chdir(folder_to_check)
folder_to_check_contents = os.listdir(folder_to_check)

# get md5 hash function. 
# check for file binary, name can be different but as long content is same, it will be found
# files cannot share the same name in a folder anyway
def file_md5(file):
    md5_hash = hashlib.md5()
    with open(file, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()

# counting initial number of files
count = 0
for file in folder_to_check_contents:
    if os.path.isdir(file) == False:
        count += 1

# init list to collect all hashes to compare with
md5_list = []

# looks through given folder and automatically deletes duplicates, leaving only first instance untouched
for file in folder_to_check_contents:
    if os.path.isdir(file) == False:
        filehash = file_md5(file)
        if filehash in md5_list:
            os.remove(file)
            print('Removing duplicates:', file)
        else:
            md5_list.append(filehash)

# count file difference
file_count_difference = count - len(md5_list)

# closing statement
if file_count_difference == 0:
    print("No duplicates found in", folder_to_check)
elif file_count_difference == 1:
    print(file_count_difference, 'file duplicate deleted in', folder_to_check)
else:
    print(file_count_difference, 'file duplicates deleted in', folder_to_check)
