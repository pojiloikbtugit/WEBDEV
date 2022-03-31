def make_bricks(small, big, goal):
  if  goal - big * 5 <= small and goal % 5 <= small:
    return True
  else: 
    return False
