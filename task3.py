def squirrel_play(temp, is_summer):
  if is_summer:
    return True if 60 <= temp and temp <= 100 else False
  else:
    return True if 60 <= temp and temp <= 90 else False
