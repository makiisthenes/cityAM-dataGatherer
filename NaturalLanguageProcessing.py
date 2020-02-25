# This will be the main program that decides whether or not a company is worth investing in or not...
# https://www.lexalytics.com/lexablog/machine-learning-natural-language-processing
# https://www.youtube.com/watch?v=FLZvOKSCkxY&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL
# https://pythonprogramming.net/tokenizing-words-sentences-nltk-tutorial/
# import nltk
# Had to manually install using nltk_data folder [INSTALLATION COMPLETE]
# C:\Users\Michael\AppData\Roaming\nltk_data
# tokenizing, grouping things...
# word tokenizer... sentence tokenizer, splits words and sentences
# coropora is just a body of text, like a bunch of text, i.e. medical journals, presidential speech, english lang
# lexicon, words and thier meanings..., doctors speak and english speak, different speak  different meaning of language text...
# <-------------------------------------------------------------------------------------------------------------------->

# TOKENIZE INTO SENTENCES AND WORDS
from nltk.tokenize import sent_tokenize, word_tokenize
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. the sky is pinkish-blue. You shouldn't eat cardboard."
print(sent_tokenize(EXAMPLE_TEXT))
print(word_tokenize(EXAMPLE_TEXT))
for word in sent_tokenize(EXAMPLE_TEXT):
    print(word)
# <-------------------------------------------------------------------------------------------------------------------->

# STOP WORDS // filters the non-useful filler words in english language... DATA PREPROCESSED
from nltk.corpus import stopwords  # ignore layout of file, used for understanding...
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))  # setting the filteration words as english language, words like, and, the
# print(stop_words)
words = word_tokenize(EXAMPLE_TEXT)
filtered_comment = []
for word in words:
    if word not in stop_words:
        filtered_comment.append(word)
print(filtered_comment)  # filtered comment from sentence, to be used...
# <-------------------------------------------------------------------------------------------------------------------->

# STEMMING // i.e riding --> rid  DATA PREPROCESSED
from nltk.stem import PorterStemmer  # its a good stemmer model
from nltk.tokenize import word_tokenize
# I was taking a ride in the car.
# I was riding in the car.
# Making the database simpler and efficient.
ps = PorterStemmer()
stemmer_words = ['python', 'pythoner', 'pythoned', 'pythonly']
for word in stemmer_words:
    print(ps.stem(word))
# stemming takes a bunch of words in which they have the same meaning but different wording and so to simplify we use it
new_text = 'It is important to be pythonly with python. All pythoners have pythoned at least once in a pythonly manner.'
words = word_tokenize(new_text)
for word in words:
    print(ps.stem(word))
# all stem from rid, and mean the same for simplifying...
# <-------------------------------------------------------------------------------------------------------------------->

# SPEECH TAGGING
import nltk
from nltk.tokenize import PunktSentenceTokenizer  # this tokenizer can me trained but its pretrained model that splits words in sentences...
sample_text = "As the pen fell far to the floor, Amy watched it hit the linoleum. She knew she couldn't have caught that pen if Brian threw it to her from his greasy old hands. But she picked it up and wrote the directions to her house. She cleared her throat, but her words still sounded hoarse."
custom_sent_tokenizer = PunktSentenceTokenizer()  # made a punkt object tokenizer that splits them into sentences, model is pretrained... in parameters you can insert training text to use for the model...
tokenized_text = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized_text:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)  # this is the key part of the code, where each individual word is tagged with function pos_tag(word_parameter...)
            print(tagged)
    except Exception as e:
        print(e)


process_content()
'''
    CC 	    coordinating conjunction
    CD  	cardinal digit
    DT  	determiner
    EX  	existential there
    FW  	foreign word
    IN  	preposition/subordinating conjunction
    JJ 	    adjective (large)
    JJR 	adjective, comparative (larger)
    JJS 	adjective, superlative (largest)
    LS  	list market
    MD  	modal (could, will)
    NN 	    noun, singular (cat, tree)
    NNS 	noun plural (desks)
    NNP 	proper noun, singular (sarah)
    NNPS 	proper noun, plural (indians or americans)
    PDT 	predeterminer (all, both, half)
    POS 	possessive ending (parent's)
    PRP 	personal pronoun (hers, herself, him,himself)
    PRP$ 	possessive pronoun (her, his, mine, my, our )
    RB  	adverb (occasionally, swiftly)
    RBR 	adverb, comparative (greater)
    RBS 	adverb, superlative (biggest)
    RP  	particle (about)
    TO 	    infinite marker (to)
    UH 	    interjection (goodbye)
    VB 	    verb (ask)
    VBG 	verb gerund (judging)
    VBD 	verb past tense (pleaded)
    VBN 	verb past participle (reunified)
    VBP 	verb, present tense not 3rd person singular(wrap)
    VBZ 	verb, present tense with 3rd person singular (bases)
    WDT 	wh-determiner (that, what)
    WP 	    wh- pronoun (who)
    WRB 	wh- adverb (how) 
'''
# <-------------------------------------------------------------------------------------------------------------------->

# CHUNKING
# You can find specific tags and bunch them up from different sentences to understand what is being said about said noun.
# 1) Named Entity - Noun - What is the sentence targeting, the subject...
# 2) Words that modify that noun, many nouns...
# A chunk is a noun covered with descriptive words that modify that specific noun.
# Look at Python Basics Regular Expression Notation...
