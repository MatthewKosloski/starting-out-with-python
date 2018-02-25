# Program 6-4
# Gets three names from the user
# and writes them to a file.

def main():

	print('Enter three names of friends.\n')

	friend1 = input('Friend 1: ')
	friend2 = input('Friend 2: ')
	friend3 = input('Friend 3: ')

	outfile = open('friends.txt', 'w')

	outfile.write(friend1 + '\n')
	outfile.write(friend2 + '\n')
	outfile.write(friend3 + '\n')

	outfile.close()
	print('Three names were written to friends.txt.')

main()