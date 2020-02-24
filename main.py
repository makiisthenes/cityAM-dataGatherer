import os
import tempfile
from pdf2image import convert_from_path
from PIL import Image
import hashlib
import requests
import datetime
import pytesseract

auto = False  # make this True when extracting new data from website automatically!!!!!!!!!
if auto:
    print('Checking Sources...')
    # make a for loop with urls and get an 200 code to confirm source is still functional and works.
    # then we can webscrape data and also download sources
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    date = str(day)+'-'+str(month)+'-'+str(year)
    if len(str(month)) == 1:
        month ='0'+str(month)
    cityam_url = 'https://www.cityam.com/wp-content/uploads/'+str(year)+'/'+str(month)+'/Cityam-'+str(year)+'-'+str(month)+'-'+str(day)+'.pdf'
    print(cityam_url)
    path_to_latest_financial_info = 'C:\\Users\\Michael\\Documents\\Coding Projects\\Python PROJECTS\\[TRADING BOT] BloomBerg CopyCat By Michael Peres\\latest_financial_info\\'
    print('Collecting Financial Data from Sources...')
    pdfnews = requests.get('https://www.cityam.com/wp-content/uploads/2020/01/CITYAM-'+str(year)+'-'+str(month)+'-'+str(day)+'.pdf')
    if pdfnews.status_code == 404:
        print('The url syntax has changed or its the weekend :( [NO TRADING DURING WEEKEND]')
        exit(-1)
    with open(path_to_latest_financial_info+'cityam'+date+'.pdf', 'wb') as f:
        f.write(pdfnews.content)
    print('Done collecting CITYAM News Source...')

filename = r'C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\[TRADING BOT] BloomBerg CopyCat By Michael Peres\latest_financial_info\cityam.pdf'
dest_path = r'C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\[TRADING BOT] BloomBerg CopyCat By Michael Peres\latest_financial_info\cityam_images'
print('Converting PDF to Images...')
with tempfile.TemporaryDirectory() as path:
    images_from_path = convert_from_path(filename, output_folder=dest_path, first_page=0)

base_filename = os.path.splitext(os.path.basename(filename))[0] + '.jpg'
for page in images_from_path:
    page.save(os.path.join(dest_path, base_filename), 'JPEG')

for file in os.listdir(dest_path):
    if file.endswith('.ppm'):
        # print(file)
        im = Image.open(dest_path+'\\'+file)
        im.save(dest_path+'\\'+file+'.jpg')
        try:
            os.remove(dest_path+'\\'+file)

        except FileNotFoundError:
            pass
print('Done obtaining images from pdf of news')
print('Junk Files have been removed.')
print('Comparing hashes of files for duplicates...')
file_count = 0
hashlist = []
list = os.listdir(r"C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\[TRADING BOT] BloomBerg CopyCat By Michael Peres\latest_financial_info\cityam_images")
for file in list:
    with open(dest_path+'\\'+file, 'rb') as afile:
        hash_var = hashlib.md5()
        buf = afile.read()
        hash_var.update(buf)
        hash = hash_var.hexdigest()
        # print(hash)
        if hash in hashlist:
            afile.close()
            os.remove(dest_path+'\\'+file)
        else:
            hashlist.append(hash)
list = os.listdir(r"C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\[TRADING BOT] BloomBerg CopyCat By Michael Peres\latest_financial_info\cityam_images")
number_files = len(list)
print(number_files)
if number_files >= 30:
    print('There is properly an error, file number is abnormally high, manually check folder in directory')
    print('[YOU SHOULD PROBABLY STOP THIS PROGRAM AND CHECK, IT COULD LEAD TO A LOSS DUE TO INVALID INFORMATION...]')
print('All duplicates have been removed,')
print('Images are being analysed for keywords...(This may take some time, depending on computers processing power.)')
with open(r'C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\[TRADING BOT] BloomBerg CopyCat By Michael Peres\latest_financial_info\text_collectionCITYAM\wordsCollectionTodayIssue.txt', 'w') as word_reseter:
    pass
files_analysed = 1
for file in list:
    img = Image.open(dest_path+'\\'+file)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    result = pytesseract.image_to_string(img) # string result...
    with open(r'C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\[TRADING BOT] BloomBerg CopyCat By Michael Peres\latest_financial_info\text_collectionCITYAM\wordsCollectionTodayIssue.txt', 'a') as word_adder:
        word_adder.write(str(result.encode('utf-8')))
    print(str(files_analysed) + ' out of ' + str(number_files) + ' pages of words have been analyised.')
    files_analysed += 1
print('Words have been collected...')
print('Analysing words and word count...')
# now we need to find words that link to companies, and use bloomberg for finding the stock-price of this company...
