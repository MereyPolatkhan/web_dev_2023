def count_code(str):
    count = 0
    i = 0
    while i < len(str) - 3:
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            count += 1
            i += 4
        else:
            i += 1
    return count
