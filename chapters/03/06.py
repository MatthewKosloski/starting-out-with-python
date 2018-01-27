# Program 3-6

# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Variables to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))

# Determine the grade.
if score >= A_score:
	print('Grade A')
else:
	if score >= B_score:
		print('Grade B')
	else:
		if score >= C_score:
			print('Grade C')
		else:
			if score >= D_score:
				print('Grade D')
			else:
				print('Grade F')