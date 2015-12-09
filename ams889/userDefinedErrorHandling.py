'''
Created on Dec 3, 2015

@author: ams889

This module contains the user defined exceptions that will be used in the program
'''

class grade_listFormatError(Exception):
    #grade_list in an incorrect format
    pass

class CamisError(Exception):
    #camis id not in dataset
    pass