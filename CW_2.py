#Task 1.1
a = input('first number: ')
b = input('second number: ')
if a > b:
  print(f'{a} is bigger than {b}')
elif a < b:
  print(f'{b} is bigger than {a}')

  #Task 1.2
a = int(input('type any number: '))
if a % 2 == 0:
  print(f'{a} is even number')
else:
  print(f'{a} is odd number')

  #Task 1.3
  a = int(input('type any number: '))
result = 1
for x in range(1, a+1):
  result *= x
 
print(f'factorial of {a} is:',result)

#Task 2.1
i = 1
while i <100:
  if i %2 == 0:
    print(i)
  i += 1