from audioop import add
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        userName = request.form['userName']
        userPassword = request.form['userPassword']
        tortillas = request.form['tortillas']
        beans = request.form['beans']
        rice = request.form['rice']
        protein = request.form['proteins']
        additional = request.form.getlist('check')
        instructions = request.form['instructions']

        print("user name", userName)
        print("user pass", userPassword)
        print("tortillas", tortillas)
        print("beans", beans)
        print("rice", rice)
        print("protein", protein)
        print("additional", additional)
        print("instructions", instructions)

        return render_template("order.html", userName=userName, userPassword=userPassword, 
        tortillas=tortillas, beans=beans, rice=rice, protein = protein, additional=additional, instructions=instructions )

app.run(debug=True)