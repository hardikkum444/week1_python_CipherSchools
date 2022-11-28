user_name, char = input('please provide your name and random char separated by commas ').split(',')


print(f'the length of your name is {len(user_name)}')
#print(f'number of char that you provided in your name are {user_name.count(char)}') #but this is case sensitive

# therefore to make it case insensitive
# we have to convert both name and char into lower case and then compare
# user_name.lower().count(char.lower)
# char.lower

print(f'number of char that you provided in your name are {user_name.lower().count(char.lower())}')