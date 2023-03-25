def caught_speeding(speed, is_birthday):
    if (is_birthday == False): 
        speed += 5
    if (speed >= 81): return 2
    if (speed >= 61): return 1
    return 0
    
