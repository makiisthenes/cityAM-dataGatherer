import hashlib
hasher = hashlib.md5()
with open(r'C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\[TRADING BOT] BloomBerg CopyCat By Michael Peres\latest_financial_info\cityam_images\7f8a9b45-8d03-4515-a278-f678d8e17ced-01.ppm.jpg', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print('Hash: '+hasher.hexdigest())
hasher = hashlib.md5()
with open(r'C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\[TRADING BOT] BloomBerg CopyCat By Michael Peres\latest_financial_info\cityam_images\8a30fef9-bd3f-49db-a57c-9fad6ea1e574-01.ppm.jpg', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print('Hash: '+hasher.hexdigest())


import os
file_count = 0
hashlist = []
list = os.listdir(r'C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\[TRADING BOT] BloomBerg CopyCat By Michael Peres\latest_financial_info\cityam_images')
for file in list:
    hasher = hashlib.md5()
    buf = afile.read()
    hasher.update(buf)
    if hasher.hexidigest in hashlist:
        os.remove('file.ext')
    else:
        hashlist.append(hasher.hexidigest)

# reality check
number_files = len(list)
if number_files > 30:
    print('There is properly an error, file number is abnormally high, manually check folder in directory')
