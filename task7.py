def make_bricks(small, big, goal):
    a = min(big, goal // 5)
    b = goal - a * 5
    if b <= small:
      return True
    else:
      return False