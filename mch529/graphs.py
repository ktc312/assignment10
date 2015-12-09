import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches
import dataManagement
from operator import add


def graphBarChart(df, boroName = "nyc"):
	df = df.astype(np.float32)
	ax = plt.subplot(111)
	w = .3		
	x = range(1,5)
	
	
	
	numGradesByYear = df['A'].values+df['B'].values+df['C'].values
	numGradesByYear.astype(float)  # needed to perform division
	
	bottomBar = list(df['A'].values / numGradesByYear)
	middleBar =list(df['B'].values / numGradesByYear)
	topBar = list(df['C'].values / numGradesByYear)

	#bar for each grade
	rectA = ax.bar( x , bottomBar, width = w, color='r', align='center')
	rectB = ax.bar(x, middleBar, width = w, color='g', align='center',bottom=bottomBar)
	rectC = ax.bar(x , topBar, width = w, color='b', align='center',bottom= map(add, bottomBar, middleBar))
	
	#set ticks and rotate text
	plt.xticks([ a + w/2 for a in  x],[val+ 2011 for val in x], rotation= 30, ha='right') 

	ax.set_xlabel('Year ', fontsize=15)
	ax.set_ylabel('Percentage of Restaurants with Grade ', fontsize=15)
	ax.set_title('Grades for Restaurants By Year in ' + str(boroName) , fontsize=15)
	ax.autoscale(tight=True)
	
	#legends
	r_patch = mpatches.Patch(color='red', label='A')
	g_patch = mpatches.Patch(color='g', label='B')
	b_patch = mpatches.Patch(color='b', label='C')
	ax.legend([r_patch,g_patch,b_patch],['A','B','C'],bbox_to_anchor=(1, .25)) #label and reposition legend
	plt.tight_layout()
	plt.savefig('grade_improvement_' + str(boroName) + '.pdf')

if __name__ =='__main__':
	print ""
	
