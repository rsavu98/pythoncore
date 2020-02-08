number = '9876'
number_list = list(number)
result = 1

for x in number_list: 
    result *= int(x)    

print(result)