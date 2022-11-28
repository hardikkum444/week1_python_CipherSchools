# to show ticket pricing 
age = int(input('enter your age '))


if age==0:
    print('You cannot watch the movie')
elif 0<age<=3:
    print('your ticket price is zero rupees')
elif 4<=age<=10:
    print('The price of your ticket is rupees 150')
elif 11<=age<=60:
    print('The price of your tickt is rupees 250')
else :
    print('The price of your ticket is rupees 200')

     