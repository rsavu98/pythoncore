#Task 1.1
a = int(input('first number: '))
b = int(input('second number: '))
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
print(f'factorial of {a} is: {result}')

#Task 2.1a
i = 1
while i <100:
  if i %2 == 0:
    print(i)
  i += 1

#Task 2.1b
i = 1
for i in range(1,100):
  if i %2 == 0:
    print(i)
  i += 1

#Task 2.2.a
for i in range(100):
  if i %2 == 0:
    continue
  print(i)

#Task 2.2.b
i=0
while i < 100:
  if i %2 ==1:
    print(i)
  i += 1    
