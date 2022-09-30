import matplotlib.pyplot as plt
import numpy as np
import math
import time
  
#these arrays are used to store the sets of respective x and y coordinates for the graphs to be drawn
totalX=[]
totalY=[]
totalColor=[]
totalLabel=[]

#this helps keep track of how many graph sets are present and the order to draw them
count=0

#introduction 
print("-----------------------------------------------------------")
print("PyPlot.py\nBy Ramithu Sellahewa\nUsing numpy and matplotlib")
print("-----------------------------------------------------------")
print("Hello! Welcome to PyPlot, which generates graphs based on values input by the user.\n")
method=int(input("Select how do you want to input data:\n1)Continous(Enter all X values first and then Y values)\n2)Alternating between X and Y\n\nSelect your option: "))
print("-----------------------------------------------------------")
i = int(input("How many graphs do you want to plot on the same axis?: "))

#this method asks for all the x vals and then goes on to y vals
if method==1:
    while (i>0):
        #input amount of coords to enter
        coordsX=int(input("How many coordinates do you want to input?:"))
        print("-----------------------------------------------------------\n")
        coordsY=coordsX #x and y coords have same amount
        #define arrays that will contain x and y coordinates
        X=[]
        Y=[]


        while (coordsX>0):
            #ask for X
            X.append(input("Enter your X value: "))
        

            coordsX=coordsX-1
        print("-----------------------------------------------------------\n")
        while (coordsY>0):
            #ask for Y
            Y.append(input("Enter your Y value: "))

            coordsY=coordsY-1
        print("-----------------------------------------------------------\n")
        #ask for color and graph label
        totalColor.append(input("what color should the graph be?: ").lower())
        totalLabel.append(input("what is the label of the graph?: ").lower())
        print("-----------------------------------------------------------\n")

        totalX.append(X)
        totalY.append(Y)    
    
    
        i=i-1
    
#this method alternates between the corresponding x and y vals
elif method==2:
    while (i>0):
        #input amount of coords to enter
        coords=int(input("How many coordinates do you want to input?:"))
        print("-----------------------------------------------------------\n")
        #define arrays that will contain x and y coordinates
        X=[]
        Y=[]


        while (coords>0):
            #ask for X and Y
            X.append(input("Enter your X value: "))
            Y.append(input("Enter your Y value: "))

            vals=vals-1

        print("-----------------------------------------------------------\n")
        #ask for color and graph label
        totalColor.append(input("what color should the graph be?: ").lower())
        totalLabel.append(input("what is the label of the graph?: ").lower())
        print("-----------------------------------------------------------\n")
        totalX.append(X)
        totalY.append(Y)    
    
    
        i=i-1
    


#plotting graphs

#using the length of the main x coordinate array in order to 
len=len(totalX)
while (len>0):
    plt.plot(totalX[count], totalY[count], color=totalColor[count], label=totalLabel[count])
    count=count+1
    len=len-1
    
print("-----------------------------------------------------------\n")

#asks labels for x and y axis, and graph title.
plt.xlabel(input("Label for X axis: "))
plt.ylabel(input("Label for Y axis: "))
plt.title(input("Title: "))

#displays legend
plt.legend()

#finally shows graph
plt.show()

