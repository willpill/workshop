def last2(s):
    if len(s) < 1:
        return 0
    last2 = s[-2:]
    count = 0
    for i in range(len(s) - 2):
        if s[i:i+2] == last2:
            count += 1
    return count