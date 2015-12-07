'''
DSGA 1007 Assignment 10
Lanyu Shang
12/08/15

This program will analyze data of the grade of each restaurant in new york city over time
and generate relevant plots to help get insight of the data.
'''

from RestaurantGrades import *
import sys


def main():
    try:
        restaurants = RestaurantGrades()
        restaurants.grade_changes()
        restaurants.print_changes()
        restaurants.count_grades()
        restaurants.plot_grades()

    except KeyboardInterrupt:
        print "Exit with interruption."
        sys.exit()
    except ArithmeticError, OverflowError:
        print "Math error occurs."
    except EOFError:
        print "EOF Error."


if __name__ =='__main__':
    main()