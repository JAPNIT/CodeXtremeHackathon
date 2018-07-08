import nltk
#noise reduction/expression removal like "lah"
lst_stop_words=open("stop_words_and_singlish.txt", "r")
stop_words=[]
for line in lst_stop_words:
    stop_words.append(''.join(line.strip().split("\n")))
lst_stop_words.close()

def _remove_noise(input_text):
    words = input_text.split() 
    noise_free_words = [word for word in words if word not in stop_words] 
    noise_free_text = " ".join(noise_free_words) 
    return noise_free_text

text="How many shrimp do you have to eat?"
words=(_remove_noise("wah why that girl so chio sia"))
print(words)

#lemmtising and stemming 
from nltk.stem.wordnet import WordNetLemmatizer 
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer 
stem = PorterStemmer()

print(lem.lemmatize(words, "v"))
print(stem.stem(words))

#word standardisation:
phrases=open("singlish_phrases.txt", "r")
singlish_phrases=[]
for line in phrases:
    singlish_phrases.append(line.strip("\n").split(","))
phrases.close()
dic_singlish={x[0]:x[1] for x in singlish_phrases}
def _lookup_words(input_text):
    words = input_text.split() 
    new_words = [] 
    for word in words:
        if word.lower() in dic_singlish:
            word = dic_singlish[word.lower()]
        new_words.append(word)
    new_text = " ".join(new_words) 
    return new_text
new_words=_lookup_words(words)
print(new_words)

#speech tagging (tagging nouns verbs adjectives adverbs)
from nltk import word_tokenize, pos_tag
tokens=word_tokenize(new_words)
print(pos_tag(tokens))

#nltk.help.upenn_tagset() #for POS tags

###topic modeling:
##doc_complete = [text, words]
##doc_clean = [doc.split() for doc in doc_complete]
##
##from gensim import gensim
##import corpora
##
### Creating the term dictionary of our corpus, where every unique term is assigned an index.  
##dictionary = corpora.Dictionary(doc_clean)
##
### Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above. 
##doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
##
### Creating the object for LDA model using gensim library
##Lda = gensim.models.ldamodel.LdaModel
##
### Running and Training LDA model on the document term matrix
##ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)
##
### Results 
##print(ldamodel.print_topics())
##


