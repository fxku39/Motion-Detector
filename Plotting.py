from Motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource



#In this block of code we create a figure object with the x axis defined as datetime type, then we adjust the size of our plot box and add a title. At last we eliminate the ticks in y-axis
# and change the value of y axis to 0 and 1
p=figure(x_axis_type='datetime', height=300, width=500, sizing_mode="stretch_width", title='Motion Graph')
p.yaxis.minor_tick_line_color=None 
p.yaxis.ticker.desired_num_ticks = 1

# We create a hovertool object and add the tooltips so we can add a label when we hover the mouse over the graphic
hover=HoverTool(tooltips=[('Start', '@start'),('End','@end')])
p.add_tools(hover)


#Creation of the quad plot
q=p.quad(left=df['start'], right=df['end'], bottom=0, top=1, color='green')

output_file('Motion_Graph.html')

show(p)