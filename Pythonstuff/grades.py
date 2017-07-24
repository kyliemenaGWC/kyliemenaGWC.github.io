#from numpy import *

# Each of our grades
kristen_grades = [90, 85, 100, 77, 94]
clarisse_grades = [96, 83, 89, 97, 86]
sapna_grades = [82, 91, 94, 87, 99]

# Class grade book
grade_book = [kristen_grades, clarisse_grades, sapna_grades]

'''
This is what our grade book looks like
[	[90, 85, 100, 77, 94]
	[96, 83, 89, 97, 86]
	[82, 91, 94, 87, 99] ]

'''

# Traverse through the grade book and print all the indivdual grades

'''for n in grade_book:
	for x in n:
		print(x)
'''
kris_avg= (sum(kristen_grades)/len(kristen_grades))
sap_avg= (sum(sapna_grades)/len(sapna_grades))
cla_avg= (sum(clarisse_grades)/len(clarisse_grades))

class_avg= [kris_avg,cla_avg,sap_avg]

print(sum(class_avg)/len(class_avg))



# Extensions: Find the class average, median, and standard deviation
# (For the extentions google for hints!)

# Super extra extensions: calculate the student with highest/lowest average
