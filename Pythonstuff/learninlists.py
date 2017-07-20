from random import randint

names = [ "beyonce","Berty","Basil","PPAP"]
last_names = ["parker", 'p','poop','mice']

names_used= []
last_names_used= []

for index in range(len(names)-1):
	rand_num1 = randint(0, len(names)-1)
	rand_num2 = randint(0,len(last_names)-1)

	random_first = names[rand_num1]
	random_last = last_names[rand_num2]

	while random_first in names_used:
		random_first = names[randint(0,len(last_names)-1)]

	while random_last in last_names_used:
		random_last = last_names[randint(0,len(last_names)-1)]	

	names_used.append(random_first)
	last_names_used.append(random_last)

	print(random_first + " " + random_last)


