# definirea unui decorator 
def print_decorator(func): 

	def inner_func_print_dec(*args, **kwargs): 
		result = func(*args, **kwargs)
		print("The result of the function is: " + str(result) )  
 	
	return inner_func_print_dec


def validate_input(func_name):

    def inner_add_function(a, b):
        if type(a) is int and type(b) is int:
            return func_name(a,b)
        else:
            print("invalid input")

    return inner_add_function



@print_decorator
@validate_input
def add(a, b):
	return a + b 



add(2,3)
add(2,None)

add(2,"Fff")

