def round10(num):
    mod = num % 10
    if mod >= 5:
        return num + (10 - mod)
    else:
        return num - mod

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)
  
