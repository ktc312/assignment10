
__author__ = "Sean D'Rosario"


"""
Submission for HW 10 for DS-GA-1007
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt






def read_data(file_name = "DOHMH_New_York_City_Restaurant_Inspection_Results.csv"):
	
	global df
	df= pd.read_csv(file_name,low_memory =False,usecols=['CAMIS','BORO','GRADE','GRADE DATE'])

	df = df.dropna() #Removing missing values

	#Removing grades other than 'A','B' and 'C', using "fancy indexing"
	mask = df.GRADE.isin(['P','Z','Not Yet Graded']) 
	df = df[~mask]

	#Removing the "Missing" borough , using "fancy indexing"
	mask = df.BORO.isin(['Missing'])
	df = df[~mask]

	#converting the string to type date-time
	df['GRADE DATE'] = pd.to_datetime(df['GRADE DATE'])

	return df


def test_grades(grade_list):

    flag = 0

    #grade_list = remove_bad_grades(grade_list)

    for i in range(1,len(grade_list)):
        current_char = grade_list[i]
        prev_char = grade_list[i-1]

        if prev_char<current_char: #'A'<'B' is True
            flag= flag-1 #Because the grade is decreasing, flag decreases by 1
        if prev_char>current_char: #'A'>'B' is False
            flag = flag +1 #Because the grade is increasing, flag increases by 1
        
    if flag>0: #Positive flag indicates that the the grades are increasing
        return 1
    if flag<0: #Negative flag indicates that the the grades are decreasing
        return -1
    return 0 #Flag=0 indicates that the the grades have stayed the same
    


def test_restaurant_grades(camis_id):

    the_list = (((df[df['CAMIS']==camis_id]).sort(columns='GRADE DATE'))['GRADE']).tolist()
    if len(the_list)==0:
        print camis_id
        return 0
    return test_grades(the_list)



def get_borough_scores():

	for borough in df['BORO'].unique().tolist():
	    list_of_camis_ids = ((df[df['BORO']==borough])['CAMIS']).unique().tolist()
	    _sum = 0
	    
	    for camis_id in list_of_camis_ids:
	        _sum = _sum+test_restaurant_grades(camis_id)
	    print "{0}'s total score is {1}".format(borough,_sum)




def restructure_dataframe(input_df):

    times = pd.DatetimeIndex(input_df['GRADE DATE'])
    year_groups = input_df.groupby([times.year,'GRADE']).size()
    year_groups = year_groups.to_frame()
    year_groups = year_groups.unstack()
    year_groups.columns = year_groups.columns.droplevel()
    return year_groups





def plotting_the_graphs():

	df_to_use = restructure_dataframe(df)
	plt.plot(df_to_use.index.values,df_to_use['A'],label="A grade")
	plt.plot(df_to_use.index.values,df_to_use['B'],label="B grade")
	plt.plot(df_to_use.index.values,df_to_use['C'],label="C grade")
	plt.xticks(df_to_use.index.values,df_to_use.index.values)
	plt.xlabel("YEAR")
	plt.ylabel("Number of restaurants")
	plt.title("Plot of all restaurants in New York City")
	plt.legend(loc = 2)
	plt.savefig("grade_improvement_nyc.pdf")

	plt.close()

	for borough in df['BORO'].unique().tolist():
	    df_to_use = restructure_dataframe(df[df['BORO']==borough])
	    df_to_use = df_to_use.fillna(0)
	    #print df_to_use
	    try:
	        plt.plot(df_to_use.index.values,df_to_use['A'],label="A grade")
	        plt.plot(df_to_use.index.values,df_to_use['B'],label="B grade")
	        plt.plot(df_to_use.index.values,df_to_use['C'],label="C grade")
	    except LookupError:
	        #print df_to_use
	        pass
	    plt.xticks(df_to_use.index.values,df_to_use.index.values)
	    plt.xlabel("YEAR")
	    plt.ylabel("Number of restaurants")
	    plt.legend(loc = 2)
	    plt.title("Plot of all restaurants in {0}".format(borough))
	    plt.savefig("grade_improvement_{0}.pdf".format(str(borough).lower()))
	    plt.close()
	    






def main():
	
	try:
		get_borough_scores()
	except:
		print "error in getting the scores of each borough"

	try:
		#plotting_the_graphs()
		print "aa"
	except:
		print "Error in plotting the graphs"

if __name__ == '__main__':
		print "Assignment10"
		read_data()
		main()

