count_rivers = {
    'nile': 'egypt', 'mississippi': 'america', 'danabube': 'germany'}


for country, river in sorted(count_rivers.items()):
	print("The " + country.title() + " river runs through " +
	river.title() + ".")
