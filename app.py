from bokeh.plotting import figure, output_file, show
from flask import Flask, render_template, request, send_from_directory, url_for
import matplotlib.pyplot as plt
import matplotlib
# import os 
matplotlib.use('Agg')
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
    fName = gName
    
    # stats = matplotlib_plot(xVal, yVal, gName, xL, yL)
    stats = create_bokeh_plot(xVal, yVal, gName, xL, yL)
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
def matplotlib_plot(xCord, yCord, gName, xL, yL):
    try:
        plt.plot(xCord, yCord, label='Data', marker='o')  
        plt.xlabel(xL)
        plt.ylabel(yL)
        plt.title(gName)
        plt.legend()
        plt.show()
        plt.savefig(f"/images/{gName}.png")

    
    # if os.path.isfile(f"images/{gName}.png"):
    #     os.remove(f"images/{gName}.png")


        
        return "gg"
    except Exception as e:
        print(f"{e} MY GODD")
        return "ded"



if __name__ == "__main__":
    app.run(debug=True)
