import string
import random
print('Введите имя, возраст и пол поочерёдно: \n')
name = input()
age = input()
gender = input()
print('Hello my name is ' '{}' ', I\'m ' '{}' ', and I\'m a ' '{}'.format(name, age, gender))
formats = 'Hello my name is ' "%s" ', I\'m ' "%s" ', and I\'m a ' "%s" % (name, age, gender)
print(formats)
about_me_fstring = f"Hello my name is {name}, I\'m {age}, and I\'m a {gender}"
print(about_me_fstring)
c = about_me_fstring.split(' ')
print(about_me_fstring)
ints=[]
ints = [x+''for x in string.ascii_letters]
for x, y in zip(ints, c):
    globals()[x] = y
list_from_str = c
print(type(list_from_str))
str_from_list = ' '.join(list_from_str)
print(about_me_fstring.swapcase())