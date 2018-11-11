dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()
print(keys)
print(values)

n = 0
for val in values:
    n += val
print(n)

print(list(keys))
print(list(values))

del dishes['eggs']
del dishes['sausage']
print(list(keys))

print(keys & {'eggs', 'bacon', 'salad'})

print(keys ^ {'sausage', 'juice'})


    
