# Program 7-9
# Calculates the average
# of values in a list.

def main():
	scores = [2.5, 7.2, 9.1, 10.1, 7.2, 5.6]

	total = 0.0

	for score in scores:
		total += score

	average = total / len(scores)

	print('Average of scores is', average)

main()