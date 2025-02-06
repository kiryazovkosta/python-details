import os.path

FILE_NANE = "for_deleting.txt"

file_path = os.path.join(os.curdir, "files", FILE_NANE)
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('File already deleted!')