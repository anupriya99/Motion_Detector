from motion import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool , ColumnarDataSource

df ["Start_String"] = df["Start"].dt.strftime("%Y-%m-%d  %H: %M: %S")
df ["End_String"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnarDataSource(df)

p=figure(X_axis_type='datetime', height=100, width=500, responsive= True, title= "Motion Graph")
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

hover = HoverTool(toolType=[("Start","@Start_string"),("End", "@End_string")])
p.add_tools(hover)

q=p.quad(left="Start",right="End",bottom=0,top=1,color="red",source=cds)

output_file("Graphic.html")
show(p)


