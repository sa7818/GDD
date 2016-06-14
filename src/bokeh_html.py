from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, BoxSelectTool
import pandas as pd
import numpy as np
import sys
import os

""" 
	This file is for handling the bokeh plots
	Two main plots min/max and gdd plots are implemented by bokeh
	In order to see the results call the functions with a file name as argument
"""


""" Plotting the bokeh plot for min max data """
def plot_minmax(fname):    
    data_frame = pd.read_csv(fname, skiprows=0, sep=",", encoding="ISO-8859-1")

    #TOOLS = [BoxSelectTool(), HoverTool(), "pan,reset, resize"]
    hover = HoverTool(
            tooltips=[
                ("index", "$index"),
                #("(x,y)", "($x, $y)"),
                ("Temp", "$y"),
            ]
        )
    p = figure(title = "Min_Max tempreture", x_axis_type="datetime", tools=[hover, "pan,reset,resize,wheel_zoom"])
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Temp'

    xdata = np.array(data_frame['Date/Time'], dtype=np.datetime64)

    p.line(xdata, data_frame["Max_Temp"], legend="Max Temp", line_color = "red")
    p.circle(xdata, data_frame["Max_Temp"], legend="Max Temp", fill_color="red", line_color="red", size=6)

    p.line(xdata, data_frame["Min_Temp"], legend="Min Temp")
    p.circle(xdata, data_frame["Min_Temp"], legend="Min Temp", fill_color="white", size=8)

    new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../csv_data/" + fname[:-4].split('/')[-1] + "_bokeh_min_max.html"
    output_file(new_fname, title="Min_Max plot")

    #show(p)
    
    return fname[:-4].split('/')[-1] + "_bokeh_min_max.html"

""" Plotting the bokeh plot for gdd data """
def plot_gdd(fname):    
    data_frame = pd.read_csv(fname, skiprows=0, sep=",", encoding="ISO-8859-1")
    
    #TOOLS = [BoxSelectTool(), HoverTool(), "pan,reset, resize"]
    hover = HoverTool(
            tooltips=[
                ("Index", "$index"),
                #("(x,y)", "($x, $y)"),
                ("GDD", "$y"),
            ]
        )
    p = figure(title = "GDD plot", tools=[hover, "pan,reset,resize,wheel_zoom"])
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'GDD'

    xdata = np.arange(0, len(data_frame["GDD"]))

    p.line(xdata, data_frame["GDD"], legend="GDD", line_color = "red")
    p.circle(xdata, data_frame["GDD"], legend="GDD", fill_color="red", line_color="red", size=6)

    p.line(xdata, data_frame["Acc_GDD"], legend="Acc GDD")
    p.circle(xdata, data_frame["Acc_GDD"], legend="Acc GDD", fill_color="white", size=8)

    
    new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../csv_data/" + fname[:-4].split('/')[-1] + "_bokeh_gdd.html"
    output_file(new_fname, title="GDD plot")

    show(p)

    return fname[:-4].split('/')[-1] + "_bokeh_gdd.html"
    

#####    
#fname = '/Users/faramarz/Desktop/CMSC6950/project/GDD/csv_data/50089_2015.csv'
#plot_minmax(fname)

#fname = '/Users/faramarz/Desktop/CMSC6950/project/GDD/csv_data/50089_2015.gdd'
#plot_gdd(fname)

try:
	fname = sys.argv[1]
	if fname[-4:] == ".csv":
		plot_minmax(fname)
	else:
		plot_gdd(fname)

except Exception as e:
	#raise e
	print(e)

