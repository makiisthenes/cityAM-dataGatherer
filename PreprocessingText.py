from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
txt_file = r'C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\[TRADING BOT] BloomBerg CopyCat By Michael Peres\latest_financial_info\text_collectionCITYAM\wordsCollectionTodayIssue.txt'
stop_words = set(stopwords.words('english'))
avoid_list = ['FTSE', 'CityAM']
filtered_words = []
with open(txt_file, 'r') as reader:
    lines = reader.readlines()
    for line in lines:
        sentences =sent_tokenize(line)
        for index in range(len(sentences)):
            words =word_tokenize(sentences[index])
            for word in words:
                if word.__contains__(r'\\n'):
                    words.remove(word)

'''
    --> Take the //n characters from a string...
    --> Get all purely number string words to be removed
    --> Also need to make it possible that stopwords are removed

'''
# print(filtered_words)
# Main problem is the text contains /n which is interferring with actual words
# and numbers are in the mix, preprocessed...
