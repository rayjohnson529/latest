toppings = []
def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	for topping in toppings:
		print("- " + topping)
	
make_pizza('pepporoni')
make_pizza('pepperoni', 'mushrooms', 'green peppers', 'extra cheese')

ingredients = []

i = 0 

while 1: 
	i+=1
	item = input('Enter item %d: '%i)
	if item == '':
		break
	ingredients.append(item)
print(ingredients)

