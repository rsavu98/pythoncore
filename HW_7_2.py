def list_animals(animals):
  counter = 1
  list = ''
  for i in animals:
      list += str(counter) + '. ' + i + '\n'
      counter+= 1
  return list   