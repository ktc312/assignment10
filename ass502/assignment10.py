'''Author: Akash Shah (ass502)
This module is the main module of the file that uses the Grades class to do the calculations 
and plotting required for this assignment'''

from grades import Grades
import sys

def main():
	#creates instance of the Grades class, which is represented by our data on restaurant grades
	grades = Grades()

	#computes and prints the sum of the grade scores in each of the boroughs and across all of NYC
	grades.compute_borough_and_city_sums()

	#plots the grade distribution amongst restaurants in each of the boroughs and across all of NYC
	grades.plot_grade_improvement_boroughs()
	grades.plot_grade_improvement_nyc()


if __name__=="__main__":
	try:
		main()
	except (KeyboardInterrupt,EOFError):
		sys.exit()
