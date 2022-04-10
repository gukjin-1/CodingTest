word = input()

li =['U','C','P','C']

check = True

for i in li:
  if i in word:
    check = True
    word = word[word.index(i)+1:]
  else:
    check = False
    break

if check == True:
  print('I love UCPC')
else:
  print('I hate UCPC')
