f = open('stopwords.txt','w')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
for i in stop_words:
    f.write(i)
    f.write("\n")
f.close()

noise_list = ["is", "a", "this"] #language stopwords (commonly used words of a language – is, am, the, of, in etc), URLs or links, social media entities (mentions, hashtags), punctuations and industry specific words.
def _remove_noise(input_text):
    words = input_text.split() 
    noise_free_words = [word for word in words if word not in noise_list] 
    noise_free_text = " ".join(noise_free_words) 
    return noise_free_text
