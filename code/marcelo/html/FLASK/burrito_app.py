from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        email= request.form['email']
        password = request.form['password']
        return base()


@app.route('/base/', methods= ['GET', 'POST'])
def base():
    return render_template('base.html')


app.run(debug=True)