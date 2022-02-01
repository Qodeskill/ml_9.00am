# Types of Plots
# There are multiple types are available to represent our data in graphical form.
# The important are:
# 1. Line Plots
# 2. Bar charts
# 3. Pie charts
# 4. Histogram
# 5. Scatter plots

# Based on input data and requirement, we can choose the corresponding plot.
# Note
# matplotlib ==> package/library
# pyplot ==> module name

# pyplot module defines several functions to create plots
# a. plot()
# b. bar()
# c. pie()
# d. hist()
# e. scatter()
# We can create plots in 2 approaches.


# We can create plots in 2 approaches.
# 1. Functional oriented approach (For small data sets)
# 2. Object oriented approach (For larger data sets)

# -->Data set is a collection of values like ndarray,python's list etc
#  wickets = [1,2,3,4,5,6,7,8,9,10]
#  overs = [1,4,5,,,..20]

# -->The values from each data set will be plotted along an axis.(x-axis,y-axis)
# matplotlib.pyplot.plot()
# import matplotlib.pyplot as plt


import matplotlib.pyplot as plt
import numpy as np
# help(plt.plot)

x = np.arange(1,11)
y = x**2
plt.plot(x,y) #(1,1),(2,4),(3,9)...
plt.show()

# How to add xlabel and ylabel to the line plot
# --> plt.xlabel() function describes inforamtion about x-axis data.
# --> plt.xlabel('N value')
# --> plt.ylabel() function describes inforamtion about y-axis data.
# --> plt.ylabel('Square of N')

x = np.arange(1,11)
y = x**2
plt.plot(x,y) #(1,1),(2,4),(3,9)...
plt.title('Square Function Line Plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.show()

# Note
# --> plt.plot(x,y) ==> To draw line plot
# --> plt.title() ==> To provide title to the line plot
# --> plt.xlabel() ==> Describes information about x-axis data
# --> plt.ylabel() ==> Describes information about y-axis data
# --> plt.show() ==> To show the line plot

## Line Plots-Advanced#
# Line properties
# --> A line drawn on the graph has several properties like color, style, width of
# the line, transparency etc. We can customize these based on our
# requirement.
# Marker property
# --> We can use marker property to highlight data points on the line plot.
# --> We have to use marker keyword argument.
# --> plt.plot(a,b,marker='o') ==> o means circle
#  ============= ===============================
#  character          description
#  ============= ===============================
#     ``'.'``    point marker
#     ``','``    pixel marker
#     ``'o'``    circle marker
#     ``'v'``    triangle_down marker
#     ``'^'``    triangle_up marker
#     ``'<'``    triangle_left marker
#     ``'>'``    triangle_right marker
#     ``'1'``    tri_down marker
#     ``'2'``    tri_up marker
#     ``'3'``    tri_left marker
#     ``'4'``    tri_right marker
#     ``'s'``    square marker
#     ``'p'``    pentagon marker
#     ``'*'``    star marker
#     ``'h'``    hexagon1 marker
#     ``'H'``    hexagon2 marker
#     ``'+'``    plus marker
#     ``'x'``    x marker
#     ``'D'``    diamond marker
#     ``'d'``    thin_diamond marker
#     ``'|'``    vline marker
#     ``'_'``    hline marker

x = np.arange(1,11)
y = x**2
plt.plot(x,y,marker='o') #(1,1),(2,4),(3,9)...
plt.title('Square Function Line Plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.show()

# Linestyle Property
# --> Specifies the line style ==> solid, dotted,dashed
# --> we can use by using linestyle keyword argument
#  plt.plot(a,b,marker='o',linestyle='--')

# **Line Styles**
#  ============= ===============================
#  character      description
#  ============= ===============================
#  ``'-'``        solid line style
#  ``'--'``       dashed line style
#  ``'-.'``       dash-dot line style
#  ``':'``        dotted line style
#  ============= ===============================

# color property
# --> By using color keyword argument we can provide colors to our plot
# --> We can specify our required color for the line plot
# --> We can use any color even hexa code also.

# matplotlib defines some short codes for commonly used colors
# --> 'b' = blue
# --> 'g' = green
# --> 'r' = red
# --> 'c' = cyan
# --> 'm' = magento
# --> 'y' = yellow
# --> 'k' = black
# --> 'w' = white

x = np.arange(1,11)
y = x**2
plt.plot(x,y,marker='o',linestyle='-',color='#77DBE6') #(1,1),(2,4),(3,9)...
plt.title('Square Function Line Plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.show()


# default color
# --> If we are not specify color then default color will be selected from the style
# circle
# --> To find the default color
#  plt.rcParams['axes.prop_cycle'].by_key()
#  blue  first default
#  orange  second default
#  green  third default
#  red  fourth default

a = np.arange(1,11)
plt.plot(x,x) # blue
plt.plot(x,x*2) # orange
plt.plot(x,x*3) # green
plt.plot(x,x*4) # red
plt.show()

# Shortcut way to set color, marker and line style
# -->We can specify the shortcut notation either mlc or clm
#  c - color
#  l - linestyle
#  m - marker
# Note
# --> In this shortcut way we should use short code for color i.e., b,g,y,k,c etc.
# --> The values red,yellow not allowed in shortcut way

x = np.arange(1,11)
y = x**2
plt.plot(x,y,'o-r') #(1,1),(2,4),(3,9)...
plt.title('Square Function Line Plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.show()

# alpha property ==> denotes opaque or transparency of the color
# value lies betweeb 0.0 to 1.0

x = np.arange(1,6)
plt.plot(x,x**3,'o-r',alpha=0.3)
plt.title('Square Function Line Plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.show()

# linewidth and marker size can be represented by using 'lw' and 'ms'
x = np.arange(1,6)
plt.plot(x,x**3,'o-g',lw=10,ms=15) # default blue color
plt.title('Square Function Line Plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.show()

# linewidth and marker size can be represented by using 'lw' and 'ms'.
# markerfacecolor ==> mfc

x = np.arange(1,6)
plt.plot(x,x**3,'o-g',lw=10,ms=15,mfc='yellow') # default blue color
plt.title('Square Function Line Plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.show()

##Sequence of Activities of plot() function
# --> Creation of figure object
# --> Creation of plot/axes object
# --> Draw x & y axis
# --> Mark evenly spaced values on x-axis and y-axis (xticks and yticks)
# --> Plot the data points
# --> connect these data points with line
# --> Add title, xlabel, ylabel
##How to customize the size of the figure
# --> The default size of the figure: 8 inches width and 6 inches height.
# --> But we can customize based on our requirement. For this we have to use
#     figure() function.

import matplotlib.pyplot as plt
help(plt.figure)

plt.figure(num=1,figsize=(10,4),facecolor='blue')
a = np.arange(1,6)
plt.plot(a,a,'o-r')
plt.show()

plt.figure(figsize=(3,3),facecolor='g')
a = np.arange(1,6)
plt.plot(a,a,'o-r')
plt.show()

# How to save line plot to a file
# --> We can save line plot to a file instead of displaying on the screen.
# --> We have to use savefig() function.
# --> Bydefault this figure will be saved in the current working directory. But we
#     can provide any location based on our requirement.
#     plt.savefig('D:\\SQ_ML\\matplotlib\\identitylineplot.jpeg')
#     help(plt.savefig)

# fig = plt.figure()
# fig.canvas.get_supported_filetypes()

#>>  27/01/2022 >>

## How to add grid lines to plot
# grid(b=None, which='major', axis='both', **kwargs)
#  Configure the grid lines.

# --> plt.grid() ==> on ==> grid lines are visible
# --> plt.grid() ==> off ==> grid lines are invisible
# --> plt.grid() ==> on ==> grid lines are visible
# --> plt.grid() ==> off ==> grid lines are invisible

# which property
# --> default is major
# --> There are major grid lines and minor grid lines are present
# --> which property will decides which grid lines are going to be displayed
# --> The allowed values are
#  which : {'major', 'minor', 'both'} ==> The default value is major.

a = np.array([10,20,30,40,50])
plt.plot(a,a,'o-r',lw=7,markersize=10,mfc='yellow')
plt.grid(color='red',lw=3)
plt.minorticks_on()
plt.grid(which='minor',color='g')
plt.show()

# axis property
# --> Along which axis, grid lines have to display
#  axis : {'both', 'x', 'y'} ==> default value: both

a = np.array([10,20,30,40,50])
plt.plot(a,a,'o-r',lw=7,markersize=10,mfc='yellow')
plt.grid(axis='y')
# plt.grid(axis='x')
plt.show()

# We can use several keyword arguments also.
#  plt.grid(color='g',lw=2,linestyle=':')

a = np.array([10,20,30,40,50])
plt.plot(a,a,'o-r',lw=7,markersize=10,mfc='yellow')
plt.grid(color='g',lw=2,linestyle=':')
plt.show()

## Adding Legend

# --> If multiple lines present then it is difficult to identify which line represents
# which dataset/function.
# --> To overcome this problem we can add legend.

a = np.arange(10)
plt.plot(a,a,marker='o',label='identity')
plt.plot(a,a**2,marker='o',label='square')
plt.plot(a,a**3,marker='o',label='cubic')
plt.legend()

# legend(labels)
# --> The argument is list of strings.
# --> Each string is considered as a lable for the plots, in the order they created.
#  plt.legend(['label-1','label-2','label-3'])
# --> This approach is best suitable for adding legend for already existing plots.

a = np.arange(10)
plt.plot(a,a,marker='o')
plt.plot(a,a**2,marker='o')
plt.plot(a,a**3,marker='o')
plt.legend(['identity','square','cubic'])
plt.show()

# Note:
# --> This approach is not recommended to use because we should aware the
# order in which plots were created.
# legend(handles, labels):
# --> We can define explicitly lines and labels in the legend() function itself.
# --> It is recommended approach as we have complete control.
#  plt.legend([line1,line2,line3],['label-1','label-2','label-3'])

a = np.arange(10)
lines = plt.plot(a,a,'o-r',a,a**2,'o-b',a,a**3,'o-g')
print(f"Type of lines : {type(lines)} ")
print(f"Lines object : ==> {lines}")


a = np.arange(10)
lines = plt.plot(a,a,'o-r',a,a**2,'o-b',a,a**3,'o-g')
print(f"Type of lines : {type(lines)} ")
print(f"Lines object : ==> {lines}")

# How to adjust legend location
# --> Based on our requirement we can decide legend location in the plot.
#  loc argument
#  loclocation
# The possible values for the location are:
# =============== =============
#  Location String Location Code
# =============== =============
#  'best'               0
#  'upper right'        1
#  'upper left'         2
#  'lower left'         3
#  'lower right'        4
#  'right'              5
#  'center left'        6
#  'center right'       7
#  'lower center'       8
#  'upper center'       9
#  'center'             10

a = np.arange(10)
lines = plt.plot(a,a,'o-r',a,a**2,'o-b',a,a**3,'o-g')
plt.legend(lines,['identity','square','cubic'],loc = 10)
plt.show()

a = np.arange(10)
lines = plt.plot(a,a,'o-r',a,a**2,'o-b',a,a**3,'o-g')
plt.legend(lines,['identity','square','cubic'],ncol=2)
plt.show()

# We can do more customization for the legend like
# --> We can add title to the legend.
# --> We can change look and feel
# --> We can change fontsize and color
# --> We can place legend outside of the plot etc

# Adding title to legend
# --> We can title for the legend explicitly. For this we have to use title
# keyword argument

a = np.arange(10)
lines = plt.plot(a,a,'o-r',a,a**2,'o-b',a,a**3,'o-g')
plt.legend(lines,['identity','square','cubic'],title='3 common functions')
plt.show()

# #How to add legend outside of the plot
# --> We can add legend outside of the plot also.
# --> For this we have to use loc keyword argument.
# loc = (x,y)
# --> loc keyword can take three types of values
# loc -> location string
# loc -> location code
# loc -> tuple of two float values ( this is to add legend to outside of the
# plot)
# --> loc=(v1,v2) -> lowest corner of Legend box

            # 0 1               1 1




            # 0 0                1 0

a = np.arange(10)
lines = plt.plot(a,a,'o-r',a,a**2,'o-b',a,a**3,'o-g')
plt.legend(lines,['identity','square','cubic'],loc=(0,1.1))
plt.tight_layout() # to fix the legend at fixed position
plt.show()


###Customization of Tick Location and Labels

# Customization of tick location and labels
# --> Ticks are the markers to represent specific value on the axis.
# --> Ticks are very helpful to locate data points on the plot very easily.
# --> Based on our input, matplotlib decides tick values automatically.
# --> Based on our requirement, we can customize tick location and labels.
# --> For this we have to use xticks() and yticks()
#  xticks(ticks=None, labels=None, **kwargs)
#  ticks  arrays like ticks location(array like)
#  labels  label for ticks location(array like)
#  kwargs  to change the text properties of the label
# --> ticks location  where we want to place the ticks
# --> ticks label  name given to the tick location
# --> calling xticks() without any argument is nothing but the getter method
# --> calling xticks() with arguments is nothing but the setter method
# Note
# --> plt.xticks([]) ==> disable the xticks
# --> plt.yticks([]) ==> disable the yticks

#* Without customizing xticks() and yticks() default values are based on the input*

a = np.arange(11)
b = a*100
plt.plot(a,b,'o-r')
plt.grid()
plt.title('Sales Report')
plt.xlabel('Year')
plt.ylabel('Number of sales')
print("Default values of xticks generated by Matplotlib based on our input values")
print(f"plt.xticks() ==> {plt.xticks()}")
print('*'*90)
print("Default values of yticks generated by Matplotlib based on our input values")
print(f"plt.yticks() ==> {plt.yticks()}")
print('*'*90)
plt.show()

# customizing xticks()
# --> plt.xticks(ticks=[0,1,2,3,4,5,6,7,8,9,10]) #to place our own xtick values
# --> For these xticks we can add labels also
# --> plt.xticks(ticks=[0,1,2,3,4,5,6,7,8,9,10],
#  labels = ['2000','2001','2002','2003','2004','2005',
#  '2006','2007','2008','2009','2010'])


a = np.arange(11)
b = a*100
plt.plot(a,b,'o-r')
plt.grid()
plt.title('Sales Report')
plt.xlabel('Year')
plt.ylabel('Number of sales')
plt.xticks(ticks= [0,1,2,3,4,5,6,7,8,9,10],
 labels= ['2000','2001','2002','2003','2004','2005', '2006','2007','2008','2009','2010']) #to place our own xtick values
# print("Values of xticks after customizationṇ ")
# print(f"plt.xticks() ==> {plt.xticks()}")
plt.show()

# We can customize label properties by using keyword arguments like color,font,size etc

a = np.arange(11)
b = a*100
plt.plot(a,b,'o-r')
plt.grid()
plt.title('Sales Report')
plt.xlabel('Year')
plt.ylabel('Number of sales')
plt.xticks(ticks= [0,1,2,3,4,5,6,7,8,9,10],
 labels= ['2000','2001','2002','2003','2004','2005', '2006','2007','2008','2009','2010'], color='blue',size=15,rotation=30,family='fantasy')
plt.show()

# customizting both xticks() and yticks()
# <<Without providing ticks values we cannot provide labels, otherwise we will get TypeError>>

a = np.arange(11)
b = a*100
plt.plot(a,b,'o-r')
plt.grid()
plt.title('Sales Report')
plt.xlabel('Year')
plt.ylabel('Number of sales')
plt.xticks(ticks= [0,1,2,3,4,5,6,7,8,9,10],
 labels= ['2000','2001','2002','2003','2004','2005', '2006','2007','2008','2009','2010'], color='blue',size=15,rotation=30,family='fantasy') 
# print("Values of xticks after customization ")
# print(f"plt.xticks() ==> {plt.xticks()}")
# print("*"*90)
plt.yticks([0,500,1000])
# print("Values of yticks after customization ")
# print(f"plt.yticks() ==> {plt.yticks()}")
# print("*"*90)
plt.show()

# disabling xticks() or yticks()
# --> If we pass empty list to xtick() or yticks() then corresponding ticks will be
# disabled on the plot
# plt.xticks([]) ==> xticks will be disabled
# plt.yticks([]) ==> yticks will be disabled


### How to set limit range of values on x-axis and y-axis
# --> By using xlim() and ylim() functions we can set limit range on axis
# For x-axis:  left and right
# For y-axis:  bottom and top
    # help(plt.xlim)
    # help(plt.ylim)

# xlim()
# Call signatures::
# --> left, right = xlim() # return the current xlim
# --> xlim((left, right)) # set the xlim to left, right
# --> xlim(right=3) # adjust the right leaving left unchanged
# --> xlim(left=1) # adjust the left leaving right unchanged
# --> If we are not passing any argument to xlim() function then it acts as
# getter function.
# --> If we are passing any argument then it acts as setter function.

a = np.arange(1,101)
b = a**2
plt.plot(a,b,'o-r')
plt.grid()
left,right = plt.xlim()
bottom,top = plt.ylim()

# print('Left limit on the x-axis:',left)
# print('Right limit on the x-axis:',right)
# print('Bottom limit on the y-axis:',bottom)
# print('Top limit on the y-axis:',top)

plt.show()

### How to set scale of x-axis and y-axis
Scaling: How to set scale for x-axis and y-axis:
 The difference between any two consecutive points on any axis is called
scaling.
 The most commonly used scales are:
 Linear scaling
 Logarithmic Scaling
# Linear scaling
# --> The difference between any two consecutive points on the given axis is
# always fixed, such type of scaling is called linear scaling.
# --> Default scaling in matplotlib is linear scaling.
# --> If the data set values are spreaded over small range, then linear scaling is
# the best choice.

# Logarithmic Scaling
# --> The difference between any two consecutive points on the given axis is not
# fixed and it is multiples of 10, such type of scaling is called logarithmic
# scaling.
# --> If the data set values are spreaded over big range, then logarithmic scaling
# is the best choice.
# --> Scaling purpose we can user plt.xscale() and plt.yscale()

a = np.arange(10000)
b = np.arange(10000)
plt.plot(a,b)
plt.grid()
plt.xscale('linear')
plt.xscale('log')
plt.show()

a = np.arange(10000)
b = np.arange(10000)
plt.plot(a,b)
plt.grid()
plt.xscale('linear')
plt.yscale('log')
plt.show()

a = np.arange(10000)
b = np.arange(10000)
plt.plot(a,b)
plt.grid()
plt.xscale('log',base=2) #logarithmic scaling
plt.yscale('log',base=9) #logarithmic scaling
plt.show()

# We can add labels to any plot by using the following 2 functions
# 1. pyplot.text()
# 2. pyplot.annotate()

# help(plt.text)


a = np.arange(10)
plt.plot(a,a,'r-o')
plt.text(2,2,'(2,2)',color='b',size=15)
plt.show()


a = np.arange(10)
plt.plot(a,a,'o-r')
for i in range(a.size): # 0 to 9
 plt.text(a[i]+0.4,a[i]-0.2,f'({a[i]},{a[i]})',color='b')
plt.show()
# -------------------------Plotting Styles-------------------------

import matplotlib.pyplot as plt
print(plt.style.available)

# --> ggplot  To emulate the most powerful ggplot style of R language.
# --> seaborn  To emulate seaborn style
# --> fivethirtyeight  The most commonly used style in real time. etc

# --------------------Bar Chart/ Bar Graph/ Bar Plot --------------------
# 1. Simple bar chart/vertical bar chart
# 2. Horizontal bar chart
# 3. Stacked Bar chart
# 4. Clustered Bar Chart/Grouped Bar Char

# Simple bar chart/vertical bar chart:
# --> The data will be represented in the form of vertical bars.
# --> Each vertical bar represents an individual category.
# --> The height/length of the bar is based on value it represents.
# --> Most of the times the width of the bar is fixed, but we can customize.
# --> The default width: 0.8
# --> By using bar() function we can create bar chart

heroes = ['Prabhas','Pawan','Chiranjeevi','Sharukh','Amitabh'] # x-axis values
movies = [100,300,200,600,1000] #height of bars, values for y-axis
plt.bar(heroes,movies)
plt.xlabel('Hero Name',color='b',fontsize=15)
plt.ylabel('Number of Movies',color='b',fontsize=15)
plt.title('Hero wise number of movies',color='r',fontsize=15)
plt.show()

heroes = ['Venkatesh','Pawan','Chiranjeevi','Sharukh','Amitabh'] # x-axis values
movies = [100,300,200,600,1000] #height of bars, values for y-axis
c = ['r','b','k','g','orange']
plt.bar(heroes,movies,color=c)
plt.xlabel('Hero Name',color='b',fontsize=15)
plt.ylabel('Number of Movies',color='b',fontsize=15)
plt.title('Hero wise number of movies',color='r',fontsize=15)
plt.show()

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
sales = [10000, 25000, 45000, 30000, 10000,
 5000,70000,60000,65000,50000]
plt.bar(years,sales,color='r')
plt.xlabel('Year',color='b',fontsize=15)
plt.ylabel('Number of Sales',color='b',fontsize=15)
plt.title('Nokia Mobile Sales in the last Decade',color='r',fontsize=15)
plt.xticks(years,rotation=30)
plt.tight_layout()
for i in range(len(years)): # 0 to 9
 plt.text(years[i],sales[i]+500,sales[i],ha='center',color='b')
plt.show()

# -------------------------Pie Chart-------------------------

marks = np.array([25,30,43,12])
plt.pie(marks)
plt.show()

marks = np.array([25,30,43,12])
mylabels = ['Python','Java','Devops','DataScience']
plt.pie(marks,labels=mylabels)
plt.show()

marks = np.array([25,30,43,12])
mylabels = ['Python','Java','Devops','DataScience']
plt.pie(marks,labels=mylabels,autopct = '%.1f')
plt.show()

marks = np.array([25,30,43,12])
mylabels = ['Python','Java','Devops','DataScience']
myexplode = [0.0,0.0,0.0,0.2]
plt.pie(marks,labels=mylabels,autopct = '%.2f%%',explode=myexplode)
plt.show()

marks = np.array([25,30,43,12])
mylabels = ['Python','Java','Devops','DataScience']
myexplode = [0.0,0.0,0.0,0.2]
mycolors = ['g','b','r','yellow']
plt.pie(marks,
 labels=mylabels,
 autopct = '%.2f%%',
 explode=myexplode,
 shadow=True,
 colors=mycolors)
plt.show()


mylabels = ['Python','Java','Devops','DataScience']
myexplode = [0.0,0.0,0.0,0.2]
mycolors = ['g','b','r','yellow']
plt.pie(marks,
 labels=mylabels,
 autopct = '%.2f%%',
 explode=myexplode,
 shadow=True,
 colors=mycolors,
 counterclock=False)
plt.legend(title='The 4 Subjects Marks')
plt.tight_layout()
plt.show()  