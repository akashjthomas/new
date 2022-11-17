dict1={ 'fruit':'mango','climate':'moderate','price(kg)':120}
dict1.pop('price(kg)')
print(dict1)

dict1.update({'fruit':'apple'})
print(dict1)
dict1.update({'car':'ford'})
print(dict1)
a=dict1.copy()
b=dict1.keys()
print(a)
print(b)
