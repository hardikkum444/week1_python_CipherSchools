# first_number = int(input('First number '))
# second_number = int(input('Second number '))
# third_number = int(input('Third number '))

num1,num2,num3 = input('Give three integer inputs separated by commas ').split(',')
avg = ((int(num1)+int(num2)+int(num3))/3)
print(f'The average of the given numbers is {avg}')