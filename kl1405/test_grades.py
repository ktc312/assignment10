# author: Kaiwen Liu

# this function returns a value based on a grade list
def test_grades(grade_list):

    initial_grade = grade_list[0]
    final_grade = grade_list[-1]
 
    if initial_grade < final_grade:
        v = -1
    elif final_grade < initial_grade:
        v = 1
    else:
        v = 0
        
    return v