def string_match(a, b):
    c = 0
    length = min(len(a), len(b))
    for i in range(length - 1):
        if a[i:i+2] == b[i:i+2]:
            c += 1
    return c