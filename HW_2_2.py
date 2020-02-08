#Task 2.1
number = input('Enter 4 character number: ')
number_list = list(number)
result = 1

for x in number_list: 
    result *= int(x)    

print(result)

#Task 2.2
number_reverse = number[::-1]
print(number_reverse)

#Task 2.3
number_sort = ''.join(sorted(number))
print(number_sort)