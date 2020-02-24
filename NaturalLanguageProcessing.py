# This will be the main program that decides whether or not a company is worth investing in or not...
# https://www.lexalytics.com/lexablog/machine-learning-natural-language-processing
# https://www.youtube.com/watch?v=FLZvOKSCkxY&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL
# https://pythonprogramming.net/tokenizing-words-sentences-nltk-tutorial/
# import nltk
# Had to manually install using nltk_data folder [INSTALLATION COMPLETE]
# C:\Users\Michael\AppData\Roaming\nltk_data
from nltk.tokenize import sent_tokenize, word_tokenize
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
print(sent_tokenize(EXAMPLE_TEXT))
