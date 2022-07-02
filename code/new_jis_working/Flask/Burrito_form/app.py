from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        tortillas=["White Flour", "Wheat Flour", "Spinach", "Corn","Bowl"]
        rice = ["White Rice", "Brown Rice", "None"]
        beans = ["Black Beans", "Pinto Beans","None"]
        protein = ["Carnitas", "Chicken", "Sofritas", "None"]
        additional_ing = ["Cheese", "Sour Cream", "Pico", "Corn","Black Olives", "Green Peppers", "Red Salasa", "Green Salsa", "Chipotle Sauce","None" ]
        return render_template("home.html", tortillas=tortillas, rice=rice, beans=beans,protein=protein,additional_ing=additional_ing)
    elif request.method == "POST":
        name= request.form["name"]
        email= request.form["email"]
        gridRadios_tortillas = request.form['gridRadios_tortillas']
        gridRadios_rice = request.form['gridRadios_rice']
        gridRadios_bean = request.form['gridRadios_bean']
        gridRadios_protein = request.form['gridRadios_protein']
        checks = request.form.getlist('check_box')
        additional_instruction= request.form["add_field"]
        print(f'Thank you {name} for your order! It will be ready in approximately 15 minutes.')
        return render_template("home.html")


app.run(debug=True)

# @app.route('/about/')
# def about():
#     return render_template("about.html")



# def home():
#     if request.method == "GET":
#         return render_template("home.html")
#     elif request.method == "POST":
#         text= request.form["text"]
#         radio = request.form['gridRadios']
#         checks = request.form.getlist('check')
#         return print ({text}... or a render_template(...))...or a redirect 