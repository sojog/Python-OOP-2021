# definirea unui decorator 
def functie_decorator(func_param): 

	#f unctie_interioara este un Wrapper (invelis)
	
	# inner function can access the outer local 
	# functions like in this case "func" 
	def functie_interioara(): 
		print("Ai ajuns in lipie") 

		# calling the actual function now 
		# inside the wrapper function. 
		func_param() 

		print("Ai terminat lipia") 
		
	return functie_interioara


# defining a function, to be called inside wrapper 
def o_functie_oarecare(): 
	print("O functie oarecare !!") 


# passing 'o_functie_oarecare' inside the 
# decorator to control its behavior 
o_functie_oarecare = functie_decorator(o_functie_oarecare) 


# chemarea functiei
o_functie_oarecare() 



@functie_decorator
def o_alta_functie(): 
	print("Aceasta este o alta functie !!") 


# # chemarea functiei
o_alta_functie() 


