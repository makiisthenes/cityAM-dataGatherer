import pytesseract
from PIL import Image

# needed to install tesseract, which allows to see the text from image
# sited: https://tesseract-ocr.github.io/tessdoc/4.0-with-LSTM.html#400-alpha-for-windows
# download file for windows: http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe
img_path = r'C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\[TRADING BOT] BloomBerg CopyCat By Michael Peres\latest_financial_info\cityam_images\04a5b21b-43b1-46f8-9ccd-776ebb60ea8a-01.ppm.jpg'
print('Image is being analyised...')
img = Image.open(img_path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
result = pytesseract.image_to_string(img)
print(result)
print('Words have been found for image.')
print(type(result))
