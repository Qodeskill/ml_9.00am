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
