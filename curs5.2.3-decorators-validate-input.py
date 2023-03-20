def validate_input(func_name):

    def inner_add_function(a, b):
        if type(a) is int and type(b) is int:
            return func_name(a,b)
        else:
            print("invalid input")

    return inner_add_function


@validate_input
def add(a,b):
    return a + b


@validate_input
def sub(a,b):
    return a - b

@validate_input
def mul(a,b):
    return a * b

print(add(2,3))

print(add(2, "32"))