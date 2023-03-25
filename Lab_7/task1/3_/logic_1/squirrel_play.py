def squirrel_play(temp, summer):
    if (temp >= 60):
      return (summer and temp <= 100) or (summer == False and temp <= 90) 
    return False
  