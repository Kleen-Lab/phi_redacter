import nltk
from nltk.corpus import words, stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Make sure resources are downloaded
nltk.download('punkt')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

# Common English dictionary words
english_words = set(words.words())
stop_words = set(stopwords.words('english'))

def filter_words_result(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)

    passed = []
    to_test = []
    not_alpha = []

    for word, tag in tagged:
        lower_word = word.lower()
        if not word.isalpha():
            return True  # Skip punctuation or numbers

        if lower_word in stop_words:
            return False
        elif tag in ('NN', 'NNP', 'NNS', 'NNPS'):  # Common noun or proper noun
        # elif tag in ('NN', 'NNS'):
            return True
        elif lower_word in english_words:
            return False
        else:
            return True

    return passed, to_test, not_alpha

def filter_words(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)

    passed = []
    to_test = []
    not_alpha = []

    for word, tag in tagged:
        lower_word = word.lower()
        if not word.isalpha():
            not_alpha.append(word)  # Skip punctuation or numbers

        if lower_word in stop_words:
            passed.append(word)
        # elif tag in ('NN', 'NNP', 'NNS', 'NNPS'):  # Common noun or proper noun
        elif tag in ('NNP', 'NNPS'):
            to_test.append(word)
        elif lower_word in english_words:
            passed.append(word)
        else:
            to_test.append(word)

    return passed, to_test, not_alpha

# Example usage
text = " Li Sam built a quantum processor near the entanglement chamber in Zurich sample lol. John emily jon na da zhang naa krum brain wide austin akshat val_mar jon_kleen valkova krum anthonyworks"
print('Categorized after word matching stage')
passed, to_test, not_alpha = filter_words(text)
print("Passed (NOT REDACTED):", passed)
print("To Test (REDACTED):", to_test)
print('Not alpha (REDACTED):', not_alpha)
