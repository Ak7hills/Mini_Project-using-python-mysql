name='akhil'
age=22
print('%s is %d years old' %(name,age))
print('{} is {} years old'.format(name,age))
print(f'{name} is {age} years old')

import datetime
now=datetime.datetime.now()
print(f'{now:%y-%m-%d-%H:%M}')

