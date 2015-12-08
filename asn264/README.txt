Author: Aditi Nair (asn264)
Date: November 28 2015


This is my submission for Assignment 10. Run the file assignment10.py to generate the solutions.
The solution to Problem (2) is in HealthDataAnalyzer.py under the function clean_health_data.
The solution to Problem (3) is in HealthDataAnalyzer.py under the function test_grades(grades).
The solution to Problem (4) is in HealthDataAnalyzer.py under the function test_restaurant_grades, print_test_results and the member functions that it calls.
The solution to Problem (5) is in HealthDataAnalyzer.py under the functions graph_grade_improvement_nyc() and graph_grade_improvement_by_boro() and in results.txt.
The solution to Problem (6) is in results.txt



Explanation for Problem (3) test_grades(grades) function: 

- I did not want to just compare the first grade issued and the last grade issued because that seemed reductive. 

- Next I tried converting the grades to integers (A, B, C to 3, 2, 1) and taking the difference between consecutive grades. If the 
differences were all zero, all non-negative, or all non-positive then I could say that the grades stayed the same, improved, or got worse.
However, since grades were not necessarily just strictly staying the same, monotonically increasing, or monotonically decreasing, I had to 
come up with a system that did not simply rely on the signs of consective differences between grades. So I considered taking casting the grades to 
integers and then taking the average of the differences. However, whether this was greater than, equal to, or less than zero amounted to seeing
whether the sum of the differences was greater than, equal to, or less than zero. A little arithmetic reveals that this is equivalent to simply
comparing the first grade and the last grade - which is reductive.

- Finally I considered implementing a system which cast the grades to integers, took the differences between the integers, and computed the
weighted average. Averages below 0 were categorized as declining, averages above zero were categorized as improving, and averages equal to zero
were categorized as staying the same.

The more recent grades would be weighted more heavily than older grades and their weights would be directly proportional to their
place in the list. I felt that this was important because we are interested in evaluating the effect of a new DOH grading system. With passing
time, presumably, the grading system would be more influential on the restaurants' behavior. Therefore we care more about recent grades.

For example, [ A B C C C] would be converted to the integers [ 3 2 1 1 1] and then to the differences [ -1 -1 0 0]. The weighted average of
this is (-1*1 + -1*2)/3 = -1 so we would categorize this as getting worse. 
