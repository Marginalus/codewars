def count_smileys(arr):
    count = 0
    smile_list = [':)', ';)', ':-)', ';-)', ':~)', ';~)', ':D', ';D', ':-D', ';-D', ':~D', ';~D']
    for i in arr:
        if i in smile_list:
            count = count + 1
    return count

print(count_smileys([':)', ';(', ';}', ':-D']))