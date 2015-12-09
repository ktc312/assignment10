from Data_work import *

'''Author: Nora Barry (neb330)'''

def main():
    '''This function will generate the six graphs of grade improvements
    in each of the fix boroughs and nyc as a whole. It will also print
    the general trend of whether restaurant grades are improving or 
    declining over NYC, and the five boroughs.'''
    
    #extract the borough names from the data set
    borough_list = list(data['BORO'].unique())[0:5]
    
    #generate the bar plots for each borough, and display general numeric trend
    for borough in borough_list:
        generate_bar_by_location(borough)
        print 'Numeric value of improving or declining restaurant grades in ' + str(borough) + ' : ' + str(sum_over_borough(borough))
        
        
    #generate the bar plot for NYC, and display general numeric trend   
    generate_bar_plot(data, 'NYC') 
    print 'Numeric value of improving or declining restaurant grades in NYC as a whole: ' +str(sum_over_restaurants(data))  
    
if __name__ == "__main__":
    main()        