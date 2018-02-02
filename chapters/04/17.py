# Program 4-17
# This program averages test scores.  It asks the user for the
# number of students and the number of test scores per student.

# Get the number of students.
num_students = int(input('How many students? '))

# Get the number of test scores per student
num_test_scores = int(input('How many test scores per student? '))

for student in range(num_students):
	total = 0.0
	print('Student number', student + 1, '\n--------------')
	for test_num in range(num_test_scores):
		print('Test number', test_num + 1, end='')
		score = float(input(': '))
		total += score

	average = format(total / num_test_scores, '.1f')

	print('Average for student number', student + 1, 'is:', average, '\n')