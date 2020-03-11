def refine_text():
    # text viewer
    has_slash = False
    text_file_path = r'C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\[TRADING BOT] BloomBerg CopyCat By Michael Peres\latest_financial_info\text_collectionCITYAM\wordsCollectionTodayIssue.txt'
    with open(text_file_path, 'r') as analysis:
        lines = analysis.readlines()
        for line in lines:
            words = line.split()
            # print(words)
            # print(type(words))
            for i in range(len(words)):
                word = words[i]
                # here we want to filter each word by looking for / and numbers but also checking whether numbers and special characters are present in the word...
                # print('--Word--')
                # i is the index of the words in the sentence....
                word = word.replace('\\n' , ' ')
                word = word.replace('\\', '')
                word = word.replace(r'\\', '')
                word = word.replace("b'", '')
                word = word.replace('  ', '')
                word = word.replace('   ', '')
                for letter in word:
                    if letter == '\\' or '\\\\':
                        has_slash = True
                        # print('Found this \\')
                    if has_slash and letter =='n':
                        # print(word)
                        word = word.replace('\\n', ' ')
                        word = word.replace('\\\\n', ' ')
                        # print('editted...')
                        # print(word)
                        has_slash = False
                words[i] = word
    # print(words)
