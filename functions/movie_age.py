#initiate the age to 0
age = 0


age = int(age)
# initiate the quitter variable to no. 
quitter = 'no'

while quitter != 'yes':
	name = input("What is your name?")
	name = str(name.title())
	while True:
		try:
			age = int(input("How old are you?"))
			break
		except ValueError:
			print("That was not a number")
	age = int(age)
	if name == "Michelle":
		print("Wait, Michelle like Michelle Johnson? Wow!")
	if age >= 21 and age < 100:
		print("Hi " + name.title() + "! You can see an R-rated movie.")
	elif age < 21 and age > 12:
		print("Hi " + name.title() + "! You can see a PG-13 movie.")
	elif age >= 100 and age < 125:
		print("Wow! " + name.title() + ", You should get into movie theatres for free.")
	elif age >= 125:
		print("You lied.")
	elif age != int:
		print("Please use only numbers.")
	else:
		print("You can only see a G-rated movie.")
	quitter = input("Would you like to end the program? Type yes to end or no to check another age.")
	
