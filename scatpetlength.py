# James Quintin 16/04/18
# Analysis of the Iris Setosa Flower from Fishers Iris Flower Dataset

import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# splits the array and takes the first 4 columns of the entire dataset
firstcol = data[:,0]
seccol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

#The first column is the petal length and split into each flower
setosaPlength = firstcol[0:50]
versicolorPlength = firstcol [50:100]
virginicaPlength = firstcol[100:150]



#calculate the mean, max, min of petal length of each flower
meanDataA = numpy.mean(setosaPlength)
meanDataB = numpy.mean(versicolorPlength)
meanDataC = numpy.mean(virginicaPlength)

minset = numpy.min(setosaPlength)
minver = numpy.min(versicolorPlength)
minvirg = numpy.min(virginicaPlength)

maxset = numpy.max(setosaPlength)
maxver = numpy.max(versicolorPlength)
maxvirg = numpy.max(virginicaPlength)


print("The average petal length of the Iris-Setosa is: ",  meanDataA)
print("The average petal length of the Iris-Versicolor is: ",  meanDataB)
print("The average petal length of the Iris-Virginica is: ",  meanDataC)

print("The minimum petal length of the Iris-Setosa is: ",  minset)
print("The minimum petal length of the Iris-Versicolor is: ",  minver)
print("The minimum petal length of the Iris-Virginica is: ",  minvirg)

print("The maximum petal length of the Iris-Setosa is: ",  maxset)
print("The maximum petal length of the Iris-Versicolor is: ",  maxver)
print("The maximum petal length of the Iris-Virginica is: ",  maxvirg)

# imported library for visualization of data
import matplotlib.pyplot as mp

# provides the x axis with a range up to 50
x = range(0,50)

# command for plotting petal length into a histogram
# argument can be changed to either flower
mp.hist(setosaPlength)
# command to print out histogram chart
mp.show()

# plots each data point to visualize general petal length of flower, adds color to each data point
se = mp.scatter(x,setosaPlength,c="b")
ve = mp.scatter(x,versicolorPlength,c="r")
vi = mp.scatter(x, virginicaPlength, c="g")

# creates a label along the y axis
mp.ylabel("Petal length in cm")

# creates a legend in the graph with appropriate colors 
mp.legend((se,ve,vi),("Setosa", "Versicolor", "Virginica"))
mp.show()