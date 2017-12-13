def is_isogram(string):
    if string is None or len(string) == 0:
        return True
    string = string.lower()
    letters = set(string)
    for l in letters:
        if not l.isalnum():
            continue
        if string.count(l) > 1:
            return False
    return True
