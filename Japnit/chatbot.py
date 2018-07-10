from nltk import word_tokenize, pos_tag, sent_tokenize, ne_chunk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tree import Tree

#Removes stopwards 
def remove_noise(input_text):
    stopword_file = open('stopwords.txt','r')
    stopwords = []
    for i in stopword_file:
        i = i.strip("\n")
        stopwords.append(i)
    stopword_file.close()
    words = word_tokenize(input_text)
    noise_free_words = [word for word in words if word not in stopwords]
    print(noise_free_words)
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text

#Text preprocessing
def pre_processing(input_text):
    input_text = remove_noise(input_text)
    words = word_tokenize(input_text)
    pos_tags = pos_tag(words)
    print(pos_tags)
    lemma = []
    for i in range(len(words)):
        w = words[i]
        try:
            pos = pos_tags[i][1]
            pos = pos[0]
            pos = pos.lower()
            print(pos)
            print(w)
            w = WordNetLemmatizer().lemmatize(w, pos)
            print(w)
            lemma.append(w)
        except:
            punctuation = [".",",","!","*"]
            if w in punctuation:
                continue
            lemma.append(w)
    text =  " ".join(lemma)

    for chunk in ne_chunk(pos_tag(word_tokenize(text))):
        if hasattr(chunk, 'label'):
            print(chunk.label(), ' '.join(c[0] for c in chunk))
         
    return text
            

def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue
    return continuous_chunk
    

