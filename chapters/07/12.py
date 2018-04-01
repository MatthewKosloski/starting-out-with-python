# Program 7-12
# Gets a series of test scores and
# calculates the average of the scores
# with the lowest score dropped.

def main():

	scores = get_scores()

	total = get_total(scores)

	lowest = min(scores)

	total -= lowest

	average = total / (len(scores) - 1)

	print('The average, with the lowest score dropped, is', average)

def get_scores():

	scores = []

	again = 'y'

	while again.lower() == 'y':
		score = float(input('Enter a test score: '))
		scores.append(score)

		again = input('Add another score? (y/n): ')
		print()

	return scores

def get_total(scores):
	total = 0
	for score in scores:
		total += score
	return total

main()
