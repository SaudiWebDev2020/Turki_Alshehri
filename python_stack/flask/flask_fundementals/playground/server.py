from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def play():
    return render_template("index_1.html")

@app.route("/play/<number>")
def play_x(number):
    return render_template("index_2.html", num = int(number))

@app.route("/play/<number>/<color>")
def play_x_color(number, color):
    return render_template("index_3.html", num = int(number), color = color)

if __name__ == "__main__":
    app.run(debug=True)