def generate_hashtag(s):
    hashArr = s.split()
    newString = ''
    for item in hashArr:
        newString += item.capitalize()
    if len(newString) > 140:
        return False
    elif len(newString) == 0:
        return False
    else:
        return '#' + newString
