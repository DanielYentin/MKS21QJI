def string_splosion(str):
  s=""
  for inc in range(len(str)+1):
    s+=str[:inc]
  return s
