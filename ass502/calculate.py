'''Author: Akash Shah (ass502)
This module contains the helper function test_grades.
A dictionary containing a numeric equivalent of each letter grade is also contained in this module,
and is used by test_grades'''

'''The motivation for the formula in test_grades is that we want we keep track of how the grade changes between consecutive 
grades which occur next to each other since grade_list is sorted by time. Thus, we numerically encode each letter and take the 
difference between consecutive grades. A positive difference is an improvement, ie C -> A is a difference of 3-1 = 2, while a 
negative difference is a decline, ie B -> C is a difference of 1-2 = -1. Finally, we weigh recent years more heavily since consumers
more often care about recent performance over historical performance. If there are n differences of consecutive grades, we do 
this by giving the most recent difference a weight of n, the second most recent a weight of n-1, and so on with the oldest
difference having a weight of 1. The final sum is the sum of all the weighted differences, normalized by the sum of the
weights. The grade list is considered improving if the sum is greater than 0, the same if the sum is equal to 0, and 
declining if it is less than 0.'''

numeric_grades={'A':3,'B':2,'C':1}

def test_grades(grade_list):
	'''computes score for a restaurant based on date-sorted grades that indicate whether the grade is 
	improving, declining, or the same over time'''

	#keeps track of the sum as we iterate through the grades data
	sum=0
	#number of grades in our list
	n=len(grade_list)

	#add or subtract "grade distance" between each pair of consecutive grades, weighing recent grades more heavily
	for i in range(0,n-1):
		sum+=(i+1)*(numeric_grades[grade_list[i+1]]-numeric_grades[grade_list[i]])/float(n*(n+1)/2)
	#sum greater than 0 indicates the grades improved over time
	if sum>0:
		return 1
	#sum equal to 0 indicates the grades stayed the same over time
	elif sum==0:
		return 0
	#sum less than 0 indicates the grades declined over time
	else:
		return -1