# a= '       Hardik      '
# b= '          **********         '
# print(a+b)
# print(a.lstrip()+b)
# print(a.rstrip()+b.lstrip())
# print(a.strip()+b.strip())
# print(a.replace(' ','')+b)

name, char= input("Enter comma seprated name and character :  ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count: {name.strip().lower().count(char.strip().lower())}")
# name.strip().lower().count(char.strip().lower())
# char.strip().lower()