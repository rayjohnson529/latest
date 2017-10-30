unconfirmed_users = ['Ray', 'Michelle', 'Peppi', 'Jim', 'Lola', 'Natalie', 'Dimmick']
# initiate empty list of confirmed users
confirmed_users = []
quitter = 'no'

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

print(unconfirmed_users)
print(confirmed_users)



while quitter != 'Yes' and quitter != 'yes':
	new_user = input("Add new user?: ")
	new_user = str(new_user)
	confirmed_users.append(new_user)
	print("Newly Confirmed Users")
	for user in confirmed_users:
		print(user)
	quitter = input("Want to quit? Type yes to quit here or no to move on.")
	
