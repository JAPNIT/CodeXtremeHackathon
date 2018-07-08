import nltk, re
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer 

stem = PorterStemmer()
lem = WordNetLemmatizer()

def noise_removal(input_text):
    noise = ["this","is",".","a"] 
    words = input_text.split()
    noise_free_words = [word for word in words if word not in noise]
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text

def remove_regex(input_text, regex_pattern):
    urls = re.finditer(regex_pattern, input_text)
    for i in urls:
        input_text = re.sub(i.group().strip(), '' , input_text)
    return input_text

regex_pattern = "#[\w]*" # can use diff patterns

text = "I am learning Natural Language Processing on Analytics Vidhya"
tokens = nltk.word_tokenize(text)
print (nltk.pos_tag(tokens))
