import string
def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = string.ascii_lowercase
    for a in alphabet:
        if a not in sentence:
            return False
    return True