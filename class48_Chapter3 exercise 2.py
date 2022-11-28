name = input('what is your name? ')
age = int(input('What is your age? '))
if age>=10 and (name[0]=='a' or name[0]=='A'):
    print('You are eligible to watch the movie coco')
else:
    print('You are not eligible to watch coco movie')