import pandas as pd
import matplotlib.pyplot as plt
import string


class RestaurantGrades:
    '''This class will analyze data of the grade of each restaurant in new york city over time
    and generate relevant plots.'''

    def __init__(self):
        #load data
        self.grades = load_data()
        self.boroughs = ['BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']
        #grade changes of five boroughs and nyc
        self.boro_changes = []
        self.total_change = 0
        #number of restaurants of each grade over time
        self.grades_counts = {'total':pd.DataFrame(index=range(2011,2016), columns=['A', 'B', 'C']).fillna(0)}
        for b in self.boroughs:
            self.grades_counts[b] = pd.DataFrame(index=range(2011,2016), columns=['A', 'B', 'C'])

    def test_restaurant_grades(self, camis_id):
        '''This function will get measure the grade change of the restaurant given camis.
        Return 1 if the grade improved and -1 if the grade dropped, otherwise return 0.'''
        restaurant = self.grades.loc[self.grades['CAMIS']==camis_id]
        return test_grades(restaurant['GRADE'])

    def grade_changes(self):
        '''This function will measure grade changes in all restaurant in nyc.'''
        #in each borough
        for b in self.boroughs:
            boro = self.grades.loc[self.grades['BORO']==b]
            camis_ids = boro['CAMIS'].unique()
            s = 0
            for i in camis_ids:
                s = s + self.test_restaurant_grades(i)
            self.boro_changes.append(s)
        #in nyc
        self.total_change = sum(self.boro_changes)

    def print_changes(self):
        '''This function will print the grade change result to console.'''
        print 'Change of all restaurants is ', self.total_change
        print 'Changes in each borough are ', zip(self.boroughs,self.boro_changes)

    def plot_grades(self):
        '''This function will plot number of restaurants in each grade
          in every borough over time by histogram. '''
        self.grades_counts['total'].plot(kind='bar', alpha=0.5)
        plt.title('NYC')
        plt.savefig('grade_improvement_nyc.pdf')
        for b in self.boroughs:
            self.grades_counts[b].plot(kind='bar', alpha=0.5)
            plt.title(b)
            plt.savefig('grade_improvement_' + string.lower(b.split(' ', 1)[0]) + '.pdf')

    def count_grades(self):
        '''This function will summarize number of restaurants in each grade in every borough over time.'''
        for b in self.boroughs:
            for y in range(2011,2016):
                counts = self.count_grades_by_year(b, y)
                self.grades_counts[b].A[y] = counts['A']
                self.grades_counts[b].B[y] = counts['B']
                self.grades_counts[b].C[y] = counts['C']
                self.grades_counts['total'].A[y] += counts['A']
                self.grades_counts['total'].B[y] += counts['B']
                self.grades_counts['total'].C[y] += counts['C']


    def count_grades_by_year(self, boro, year):
        '''This function will count number of restaurants in each grade in a given borough of a given year.'''
        sub = self.grades[(self.grades.BORO==boro) & (self.grades.YEAR <= year)]
        camis_ids = sub.CAMIS.unique()
        counts = {'A':0, 'B':0, 'C':0}
        for i in camis_ids:
            counts[sub[sub.CAMIS==i].GRADE.values[0]] += 1
        return counts


def load_data():
    '''this function will load data and clean invalid entries'''
    #load data
    df = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', index_col=False,
                     dtype={'PHONE': str})
    df = df[['CAMIS', 'BORO', 'GRADE', 'GRADE DATE']]
    #remove rows with invalid Grade, Borough and GRADE DATE
    df = df.loc[df['GRADE'].isin(['A', 'B', 'C'])]
    df = df.loc[df['BORO'].isin(['BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND'])]
    df = df.dropna(subset=['GRADE DATE'])
    df = df.drop_duplicates()
    #extract year from GRADE DATE
    df['YEAR'] = df['GRADE DATE'].apply(lambda date: int(date[-4:]))

    return df


def test_grades(grade_list):
    '''This function will measure the grade change in grade_list
    return 1 if the grade improved and -1 if the grade dropped, otherwise return 0.'''
    if len(grade_list) == 1:
        return 0
    else:
        index = 0
        for i, j in zip(grade_list, grade_list[1:]):
            if i < j:
                index += 1
            elif i > j:
                index -= 1

        if index > 0:
            return 1
        elif index < 0:
            return -1
        else:
            return 0
