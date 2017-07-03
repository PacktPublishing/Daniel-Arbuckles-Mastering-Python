def tabs_cause_problems():
    with open('test.txt') as f:
	for line in f:
	    try:
		print(int(line))
	    except ValueError:
		print('Not an integer')

