from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        email= request.form['email']
        password = request.form['password']
        return burrito()


@app.route('/burrito/', methods= ['GET', 'POST'])
def burrito():
    return render_template('burrito.html')


app.run(debug=True)