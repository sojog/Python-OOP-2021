# definirea unui decorator 
def print_decorator(func): 

	def inner_func_print_dec(*args, **kwargs): 
		result = func(*args, **kwargs)
		print("The result of the function is: " + str(result) )  
 	
	return inner_func_print_dec


@print_decorator
def add_two_members(a, b):
	return a + b 


def another_add_two_members(a, b):
	return a + b 


add_two_members(2,3)

another_add_two_members = print_decorator(print_decorator)

