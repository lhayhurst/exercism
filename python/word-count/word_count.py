import re

def word_count(phrase):
    words = re.split(',\n|;|,|_|\s*:*\s*|\s*', phrase)
    cnt = {}
    stripchars = ",:.\'\""
    for w in words:
        #strip any leading and trailing non alphanumeric characters
        w = w.lower()
        w = re.sub(r"^\W+|\W+$", "", w)
        if w not in cnt:
            cnt[w] = 0
        cnt[w] += 1
    return cnt
