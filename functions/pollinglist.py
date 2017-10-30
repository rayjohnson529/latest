responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	response = input("\nWhat mountain would you like to climb someday? ")
	
	responses[name] = response
	
	repeat = input("Would you like to let another person answer poll [yes/no]")
	if repeat == 'no':
		polling_active = False
		
	print("\n--- Poll Results ---")
	for name, response in responses.items():
		print(name + " would like to climb " + response + ".")
		
