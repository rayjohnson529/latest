with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)

filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		# to remove the white space between lines
		print(line.rstrip())
