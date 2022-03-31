def parrot_trouble(talking, hour):
  if talking and hour < 7 or talking and hour > 20:
    return True
  elif talking and hour > 7 or talking and hour < 20: 
    return False
  else: return False
