# -*- coding: utf-8 -*-
"""Data Visualization and Summary Statistics .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JuwbKXF6kU5RMZpnAprBIfoaFNaPaQ5S

Data Visualization using Python

importing pandas library
"""

import pandas as pd

"""Creating Dataframe using Python Dictionary"""

result = {
    ' Students\' Name' : ['ABC', 'AQW', 'NHY', 'CBY', 'SPO','LHG','NZR','MLG','AUF','DDX'],
    ' Maths' : [50,84,56,88,63,93,56,65,78,89],
    ' Electronic Circuits ' : [70,62,98,95,55,85,45,59,43,67],
    ' Signals and Systems ' : [64,75,45,76,56,71,75,45,76,62],
    ' Analog Communication ' : [43,46,61,84,84,65,46,61,84,75],
    ' Digital Electronics ' : [51,74,73,79,95,58,74,73,79,46],
    
}

"""Creating Dataframe Object """

df = pd.DataFrame(result)
df

"""Bar Graph for Electronics Circuits with Students' Name"""

import matplotlib.pyplot as plt

plt.bar(df[' Students\' Name'],df[' Electronic Circuits '])
#To add title to graph
plt.title(" Bar Graph ")

#To add labels to X and Y axes
plt.xlabel(" Students\' Name ")
plt.ylabel(" Electronic Circuits Marks ")

#To display the graph
plt.show()

"""Analysis = \
1)NHY is top scorrer for Electronics Circuits.  
2)AUF need to improve in Electronics Circuits. \
3)3 students are having marks above 80.

Resource = https://www.geeksforgeeks.org/data-visualization-with-python/

Scatter Plot of Signals and Systems with Students' Name
"""

plt.scatter(df[' Students\' Name'],df[' Signals and Systems '])
#To add title to graph
plt.title(" Scatter Plot ")

#To add labels to X and Y axes
plt.xlabel(" Students\' Name ")
plt.ylabel(" Signals and Systems Marks ")

plt.show()

"""Analysis = \
1)NHY and MLG need to improve. \
2) Density of marks obtained by students is mostly in upper half of graph region indicating good scores by students in Signals and Systems subject.

Histogram of Maths with Students' Name
"""

plt.hist(df[' Maths'])
#To add title to graph
plt.title(" Histogram ")

#To display the graph
plt.show()

"""Line Graph of Analog Communication and Maths Marks Combined"""

# Multiple Line Plots in Single Plot
plt.plot(df[' Maths'])
plt.plot(df[' Analog Communication '],'-.')
#To add title to graph
plt.title(" Line Chart ")

#To display the graph
plt.show()

"""Pie Chart of Digital Electronics with Students' Name"""

import numpy as np

#The explode feature allows separating the slices of the piechart.
# Creating explode data
explode = (0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.0)

# Creating color parameters
colors = ( "orange", "cyan", "brown",
          "grey", "indigo", "beige", "red","blue","green","gold")

#To determine properties of border line
# Wedge properties
wp = { 'linewidth' : 1, 'edgecolor' : "black" }

#autopct enables you to display the percent value using Python string formatting
# Creating autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)

# Creating plot
#figsize is a tuple of the width and height of the figure in inches,To create an 800x400 pixel, fig = plt. figure(figsize=(8,4))
#pyplot. subplots method provides a way to plot multiple plots on a single figure.Given the number of rows and columns,
#   it returns a tuple (fig,ax), giving a single figure fig with an array of axes ax .
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(df[' Digital Electronics '],
                                  autopct = lambda pct: func(pct, df[' Digital Electronics ']),
                                  explode = explode,
                                  labels = df[' Students\' Name'],
                                  shadow = True,
                                  colors = colors,
                                  startangle = 90,
                                  wedgeprops = wp,
                                  textprops = dict(color ="magenta"))

# Adding legend
ax.legend(wedges, df[' Students\' Name'],
          title ="Students Name",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Customizing pie chart")
 
# show plot
plt.show()

"""Summary Statistics

Mean : The mean is more commonly known as the average.
"""

import pandas as pd

mean = df[' Maths'].mean()
print(mean)

"""The Median is the mid-point in a distribution of values among cases, with an equal number of cases above and below the median."""

median = df[' Maths'].median()
print(median)

"""The mode is the value that occurs most often in the distribution"""

mode = df[' Maths'].mode()
print(mode)

"""**Variance** \
In statistics, the variance is a measure of how far individual (numeric) values in a dataset are from the mean or average value.

A **high variance** tells us that the values in our dataset are far from their mean. So, our data will have **high levels of variability**. \
On the other hand, a **low variance** tells us that the values are quite close to the mean. In this case, the data will have **low levels of variability**.
"""

var = df[' Maths'].var()
print(var)

"""**Standard Deviation**

The standard deviation measures the amount of variation or dispersion of a set of numeric values.

**Low values** of standard deviation tell us that individual values are **closer to the mean**. \
**High values**, on the other hand, tell us that individual observations are **far away from the mean** of the data.

Values that are within one standard deviation of the mean can be thought of as fairly typical, whereas values that are three or more standard deviations away from the mean can be considered much more atypical. They're also known as **outliers**.
"""

stdDev = df[' Maths'].std()
print(stdDev)