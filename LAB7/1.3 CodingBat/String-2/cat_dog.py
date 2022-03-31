def cat_dog(str):
  dogcnt = 0
  catcnt = 0 
  for i in range(len(str) - 2):
    if str[i:i+3] == "cat":
      catcnt += 1
    elif str[i:i+3] == "dog":
      dogcnt += 1
  if catcnt == dogcnt:
    return True
  return False