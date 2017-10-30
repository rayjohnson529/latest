to_be_polled_people = ['Michelle', 'Dimmick', 'Jim', 'Natalie']

polled_people = {'Michelle': 'Python', 'Dimmick': 'COBOL'}

for name in to_be_polled_people:
	if name  in polled_people:
		print(name.title() + ", we see you like " + polled_people[name].title() +
		". Thank you for taking our Survey.")
	else:
		print(name.title() + ", please take our survey.")
