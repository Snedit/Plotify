from bokeh.plotting import figure, output_file, show
from flask import Flask, render_template, request

from bokeh.models import ColumnDataSource


app = Flask(__name__)
# app('/static', '/path/to/static')
@app.route("/")
def index():
    return render_template("index.html") 

@app.route('/process', methods=['POST'])
def process():
    xVal = request.form.getlist('x_axis')
    yVal = request.form.getlist('y_axis')
    
    gName = request.form.get('graphName')
    xL = request.form.get('x_label') 
    yL = request.form.get('y_label') 
    print(xVal, yVal, gName, xL, yL)
    gChoice = request.form.get('choose')
    if(gChoice == "line"):
    # stats = matplotlib_plot(xVal, yVal, gName, xL, yL)
        stats = create_bokeh_plot(xVal, yVal, gName, xL, yL)
    elif gChoice == "scatt":
        stats = create_scatter_plot(x=xVal, y= yVal, x_label=xL, y_label=yL, title=gName)

    print(stats)
    
    if stats != "DED":
        show(stats)
        return render_template(f"success.html")
    else:
        return render_template("error.html")
    # if stats == "gg":
    #     target = gName + ".png"
    #     return render_template("success.html", target=target) 
    # elif stats == "ded":
    #     return render_template("error.html")


def create_scatter_plot(x, y, title, x_label, y_label):
    try:
        p = figure(title=title, tools="pan,box_zoom,reset,save", x_axis_label=x_label, y_axis_label=y_label)
        source = ColumnDataSource(data=dict(x=x, y=y))

        p.circle('x', 'y', source=source, size=10, color="navy", alpha=0.5)
        p.x_range.start = -1  # Adjust this value as needed
        p.x_range.end = 6  # Adjust this value as needed
        p.y_range.start = 0  # Adjust this value as needed
        p.y_range.end = 10  # Adjust this value as needed
        output_file(f"{title}.html")
        return p
    except Exception as e:
        print(e)
        return 'DED'

def create_bokeh_plot(x_values, y_values, graph_name, x_label, y_label):
    try:
        # Create a Bokeh figure
        p = figure(title=graph_name, x_axis_label=x_label, y_axis_label=y_label)

        # Add data to the plot
        p.line(x_values, y_values, line_width=2)

        # Generate the plot as an HTML file (you can customize the filename)
        output_file(f"{graph_name}.html")
        
        # Display the plot in a web browser
        return p  # Success
        
        
    except Exception as e:
        print(e)
        return "DED"  # Failure


@app.route('/reClick')
def reclick():
    return render_template("/index.html")
 















# @app.route('/matplotlib_plot')
# def matplotlib_plot(xCord, yCord, gName, xL, yL):
#     try:
#         plt.plot(xCord, yCord, label='Data', marker='o')  
#         plt.xlabel(xL)
#         plt.ylabel(yL)
#         plt.title(gName)
#         plt.legend()
#         plt.show()
#         plt.savefig(f"/images/{gName}.png")

    
#     # if os.path.isfile(f"images/{gName}.png"):
#     #     os.remove(f"images/{gName}.png")


        
#         return "gg"
#     except Exception as e:
#         print(f"{e} MY GODD")
#         return "ded"



if __name__ == "__main__":
    app.run(debug=True)
