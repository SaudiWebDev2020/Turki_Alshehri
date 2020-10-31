from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_8x8():
    return render_template("index.html", x = 8, y = 8)

@app.route('/<x>')
def display_x(x):
    x = int(x)
    return render_template("index.html", x = int(x), y = int(x))

@app.route('/<x>/<y>')
def display_x_y(x,y):
    return render_template("index.html", x = int(x), y = int(y))

if __name__ == "__main__":
    app.run(debug=True)
