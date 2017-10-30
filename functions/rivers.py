count_rivers = {
    'nile': 'egypt', 
    'mississippi': 'america',
    'danabube': 'germany'}
    
print("The following rivers have been mentioned: ")
for river in count_rivers.keys():
	print(river.title())
	
print("\nThe following countries have been mentioned: ")
for country in count_rivers.values():
	print(country.title())




for country, river in sorted(count_rivers.items()):
	print("\nThe " + country.title() + " river runs through " +
	river.title() + ".")

