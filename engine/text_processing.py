
# helpers/text_processing.py
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [WordNetLemmatizer().lemmatize(word.lower()) for word in tokens if word.isalnum() and word.lower() not in stop_words]
    return ' '.join(tokens)

def calculate_similarity(input_str, target_str):
    input_set = set(input_str.split())
    target_set = set(target_str.split())
    intersection = len(input_set.intersection(target_set))
    union = len(input_set.union(target_set))
    if union != 0:
        similarity = intersection / union
    else:
        similarity = 0.0
    return similarity
