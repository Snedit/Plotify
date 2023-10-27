from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os 

app = Flask(__name__)

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
    
    stats = matplotlib_plot(xVal, yVal, gName, xL, yL)
    
    if stats == "gg":
        return render_template("success.html", target=f"{gName}") 
    elif stats == "ded":
        return render_template("error.html")

@app.route('/matplotlib_plot')
def matplotlib_plot(xCord, yCord, gName, xL, yL):
    try:
        plt.plot(xCord, yCord, label='Data', marker='o')  
        plt.xlabel(xL)
        plt.ylabel(yL)
        plt.title(gName)
        plt.legend()
        
        
        if os.path.isfile(f"images/{gName}.png"):
            os.remove(f"images/{gName}.png")


        plt.savefig(f"images/{gName}.png")
        
        return "gg"
    except:
        return "ded"

if __name__ == "__main__":
    app.run(debug=True)
