# Program 6-1
# This program writes three lines of data
# to a file.

def main():
	# Open a file
	outfile = open('philosophers.txt', 'w')

	# Write to the file
	outfile.write('John Lock\n')
	outfile.write('David Hume\n')
	outfile.write('Edmund Burke\n')

	# Close the file
	outfile.close()

main()