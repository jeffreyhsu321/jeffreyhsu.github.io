'''
Title: Investigate Data Project
Names: Jeffrey Hsu, Arianna McDonald
Date: Feburary 09, 2017
'''

import matplotlib.pyplot as plt
import os.path
import math
import random as r # used to generate random colors for pie chart

# Get the directory name for data files
directory = os.path.dirname(os.path.abspath(__file__))  

#------rng for color------#
colorAll=[]
interval=(.09)
R=r.uniform(0, 0.5)
G=r.uniform(0, 1)
B=r.uniform(0, 0.5)

for i in range(15):      #gradient
    colorAll.append((R,G,B,1))
    #if ((B+interval)>1):
        #interval=interval*(-1)
    B=B+interval
    R=R+interval
    
#------data reading------#
# Open the file
filename = os.path.join(directory, 'Depression.csv')
datafile = open(filename,'r')

#initialize aggregators
improvementlist = []
roundedImprovement = []

for line in datafile:
    Names, Year, OGScore, NewScore, Improvement, College = line.split(',')
    improvementlist.append(int(Improvement))
    
#Close file
datafile.close()

#------data manipulation------#
for num in improvementlist:
    roundedImprovement.append((math.floor(int(num)/100))*100)  #rounds up the data

sizes=[]
for i in range(9):
    sizes.append(roundedImprovement.count(i*100))   #sum up the number of occurences

sizes[5] = sizes[5] + sizes[6] + sizes[7] + sizes[8]
sizes.remove(sizes[8])
sizes.remove(sizes[7])
sizes.remove(sizes[6])

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=('0~90','100~190','200~290','300~390','400~490','500~890'), autopct='%1.1f%%', shadow=True, startangle=90, colors=colorAll)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

persisted = []
scoreRange = []

#------long term------#
filename = os.path.join(directory, 'LongTerm.csv')
datafile = open(filename,'r')
for line in datafile:
    scoreRangeStudent, ph, ph2, ph3, persistedStudent, ph4= line.split(',')
    persisted.append(persistedStudent)
    scoreRange.append(scoreRangeStudent)
datafile.close()

fig2, ax2 = plt.subplots(1, 1)
N = 3
x = range(N)
width = 1/1.5
ax2.bar([1,2,3], persisted, width, color=colorAll[0])
ax2.set_xticks([1,2,3], scoreRange)
ax2.set_xlabel('SAT Scores')
ax2.set_ylabel('Number of Students Persisting to Second Year')
ax2.set_title('Number of Students Persisting to Second Year vs SAT Scores')
ax2.legend()
plt.show()