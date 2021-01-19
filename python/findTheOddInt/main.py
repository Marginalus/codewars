from collections import Counter

def find_it(seq):
    new_tuple = Counter(seq)
    for key in new_tuple:
        if(new_tuple[key] % 2 != 0):
           return key
