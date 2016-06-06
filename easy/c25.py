''' r/dailyprogrammer [Easy] Challenge 25: majority vote'''

def winner(votes):
	A = 0
	B = 0

	'''count votes'''
	for vote in votes:
		if vote == "A":
			A += 1
		else:
			B += 1

	'''determine winner'''
	if A == B:
		print "No winner."
	elif A > B:
		print "Candidate A wins."
	else:
		print "Candidate B wins."

votes = ["A", "A", "B", "A", "B" "B", "A", "A", "B", "A"]
winner(votes)