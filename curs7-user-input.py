
# lambda este o functie anonima 
add = lambda x, y: x + y
print(add)
print(type(add))
print(add(2, 3))


# # Map
map_result = map(lambda a: a**2, [1, 2, 3, 4, 5])
print(map_result)
print(type(map_result))
x = list(map_result)
print(x)


# ## Map
y = list(map(lambda a, b: a+b, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
print(y)


lst = [{'name': 'Bob', 'age': 30}, {'name': 'Matt', 'age': 40}]
z = list(map(lambda a: a['name'], lst))
print(z)


# # Filter
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst = list(filter(lambda x: (x % 2 == 0), li))
print(lst)

# # Reduce
from functools import reduce
li = [1, 2, 3, 4, 5]
sum = reduce((lambda x, y: x + y), li)
print(sum)


todo = ["0", "10", "3", "azi"]

lst = list(filter(lambda elem: elem.isnumeric(), todo))
lst = list(map(lambda x : int(x), lst))
lst = reduce((lambda x, y: x+y), lst)

lst2 = reduce(
    (lambda x, y: x+y), 
    map((lambda x : int(x)), 
    (filter(lambda elem: elem.isnumeric(), todo)
)))
print(lst2)


def add(a, b, *args, **kwargs): 
    list_of_parameters = list(args).extend(list(kwargs.values()))
    args_sum = 0 if len(args) == 0 else reduce(lambda x, y: x + y, list_of_parameters )

    sum = a + b + args_sum
    print(sum)


add(1, 1, p = 6)
# add(2, 5, 7, 8, 3, 9)

def printable(func_param): 
	def functie_interioara(*args, **kwargs): 
		print(func_param(*args, **kwargs)) 
	return functie_interioara


@printable
def add_v2(*args, **kwargs):
    values = (value for value in kwargs.values())
    total = reduce(lambda x, y: x+y, args)
    return total + reduce(lambda x, y : x+y, values)

@printable
def add_v3(*args, **kwargs):
    values = [value for value in kwargs.values()]
    list(args).extend(values)
    return reduce((lambda x, y: x+y), values )


add_v2(3, 4, 5, p = 5)
add_v3(2,3, p = 3)
# add_v2(5,5)
# add_v2(5,5,5,5,5,5,5,5)