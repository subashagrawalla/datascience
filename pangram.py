def is_pangram(sentence):
    
    alphalist='abcdefghijklmnopqrstuvwxyz'

    for i in alphalist:
        if i not in sentence.lower():
            return False

    return True



