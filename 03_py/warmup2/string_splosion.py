def string_splosion(str):
  a = ""
  for i in range(len(str) + 1):
    a+=str[:i]

  return a
