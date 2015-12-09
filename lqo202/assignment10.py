"""
This part generates the results, it launches an small interfase where the user has to write 1 to display results or q to quit.
Once all is launched, it returns to the menu.
Exception handling and input validation is done for each part.
IMPORTANT : The input MUST be in the same directory as this .py file
"""

__author__ = 'lqo202'

import Clean_DB as clean
import Grade as g
import pandas as pd
from matplotlib import pyplot as plt


##### Previous functions to validate input, handle exceptions and launch the result####
def printingresults1(grades_db):
    print 'Grades of restaurants by boro:'
    try:
        for boro in list(grades_db.BORO.unique()):
            filtered = grades_db[grades_db['BORO']==boro]
            #Results of scores
            total = filtered.test_restaurant_in_boro(boro)
            print "Score in %s is %i" %(boro, total)
            #Plot
            filtered.plot_by_boro(boro)
            if boro != list(grades_db.BORO.unique())[-1]:
                print "Close window to continue displaying"
            plt.show()
    except ValueError:
        print "Oops!  That was no valid input.  Try again!"
    except ArithmeticError:
        print 'ArithmeticError ocurred in boros'
    except LookupError:
        print 'LookupError ocurred in boros'
    except AttributeError:
        print 'Attribute error in boros'
    except TypeError:
        print 'Type Error in boros'

def printingresults2(data):
    print 'Results for NYC, processing...'
    try:
        #Plotting
        graph = data.plot_by_boro()
        plt.show()
        print 'Showing and saving graph of evolution of grades in restaurants in NYC'

        #Calling results by boro
        printingresults1(data)
    except KeyboardInterrupt:
        print 'Keyboard interrupted, try again!'
    except ArithmeticError:
        print 'ArithmeticError ocurred results NY'
    except LookupError:
        print 'LookupError ocurred results NY'
    except ValueError:
        print 'Value error ocurred in results BY'

########### Importing the DB ############
def import_data(file ="DOHMH_New_York_City_Restaurant_Inspection_Results.csv"):
    #Uploading DB, just columns needed
    #Type of vars where found on the URL of the database
    db_types = {'CAMIS':str,
                'BORO': str,
                'GRADE': str,
                'GRADE DATE': str}
    ratings = pd.read_csv(file, usecols= ['CAMIS', 'BORO', 'GRADE', 'GRADE DATE'], dtype=db_types)
    return  ratings



############## Final screening of results #########
def mainwindow():
    print 'Restaurants in NYC info: Assignment 10 - Programming for Data Science'
    while True:
        try:
             optionuser = raw_input('Menu: Press 1 to start showing some plots and results, q for exit   :')
             if optionuser == 'q': break
             else:
                 if int(optionuser) == 1:

                    ratings =  import_data()

                    #Creating CleanDB object and cleaning
                    ratings_db = clean.clean_DB(ratings)
                    rating_clean = ratings_db.clean_all()

                    #Creating grades object
                    grades_db = g.grades(rating_clean)
                    print "Data was cleaned! Processing ..."

                    #Calling NYC results
                    printingresults2(grades_db)

                 else:
                     print "That option was not valid, try again!"
        except ValueError:
            print "Oops!  That was no valid input.  Try again with a number!"
        except KeyboardInterrupt:
            print 'Keyboard interrupted, try again!'
        except IOError:
            print 'File not found!'



if __name__ == "__main__":
    try:
        mainwindow()
    except EOFError:
        pass
