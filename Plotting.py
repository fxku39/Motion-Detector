from Motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

#We create new columns in the df utilizing the already existing columns 'start' and 'end'. The new columns then have the datetime formated and passed to the hover tool
df['Start_string']=df['start'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['End_string']=df['end'].dt.strftime('%Y-%m-%d %H:%M:%S')

cds=ColumnDataSource(df)

#In this block of code we create a figure object with the x axis defined as datetime type, then we adjust the size of our plot box and add a title. At last we eliminate the ticks in y-axis
# and change the value of y axis to 0 and 1
p=figure(x_axis_type='datetime', height=300, width=500, sizing_mode="stretch_width", title='Motion Graph')
p.yaxis.minor_tick_line_color=None 
p.yaxis.ticker.desired_num_ticks = 1

# We create a hovertool object and add the tooltips so we can add a label when we hover the mouse over the graphic
hover=HoverTool(tooltips=[('Start', '@Start_string'),('End','@End_string')])
p.add_tools(hover)


#Creation of the quad plot
q=p.quad(left='start', right='end', bottom=0, top=1, color='green', source=cds)

output_file('Motion_Graph.html')

show(p)
