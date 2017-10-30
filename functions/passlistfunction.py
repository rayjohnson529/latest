def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'Margrot']
greet_users(usernames)
