import re
import pickle
from sklearn.feature_extraction.text import HashingVectorizer

stop = pickle.load(open('./imdb/pkl_objects/stopwords.pkl', 'rb'))
clf = pickle.load(open('./imdb/pkl_objects/classifier.pkl', 'rb'))

# Run the pre process functions

def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',
                           text.lower())
    text = re.sub('[\W]+', ' ', text.lower()) + \
        ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized


vect = HashingVectorizer(decode_error='ignore',
                         n_features=2**21, preprocessor=None, tokenizer=tokenizer)


