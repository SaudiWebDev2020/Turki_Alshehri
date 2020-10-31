from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe'

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
    print(request.form['values'])
    session['choice'] = request.form['values']
    return redirect('/result')


@app.route('/result')
def result():
    # print(request.form['values'])
    # session['choice'] = request.form['values']
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True) 