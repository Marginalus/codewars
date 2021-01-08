def unique_in_order(iterable):
    new_arr = []
    for i in range(len(iterable)):
        if i == 0:
            new_arr.append(iterable[i])
        elif iterable[i] != iterable[i-1]:
            new_arr.append(iterable[i])
        
    return new_arr
    

print(unique_in_order('AAAABBBCCDAABBB'))