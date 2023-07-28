import lib

values=input('Enter values seperated by comma:')
values=[eval(val) for val in values.split(',')]
print(values)