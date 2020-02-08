number = input('Enter 4 character number: ')
number_list = list(number)
result = 1

for x in number_list: 
    result *= int(x)    

print(result)

number_reverse = number[::-1]
print(number_reverse)

number_sort = ''.join(sorted(number))
print(number_sort)