print("Welcome to my Calculator!!")
print('1: ', 'Addition')
print('2: ', 'Substraction')
print('3: ', 'Multiplication')
print('4: ', 'Division\n')

select_opt = input('Please select an Option!: ')

num1 = int(input('Please enter your first number: '))
num2 = int(input('Please enter your second number: '))


if select_opt == '1':
    print(num1 + num2)
elif select_opt == '2':
    print(num1 - num2)
elif select_opt == '3':
    print(num1 * num2)
elif select_opt == '4':
    print(num1 / num2)
else:
    print('Invalid number!')

