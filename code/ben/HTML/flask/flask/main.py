from flask import Flask, redirect, url_for, render_template, request 

app = Flask(__name__)

@app.route("/")
def home():
    title = "The Burrito Shop"
    return render_template("index2.html", title=title)

@app.route("/order")
def order():
    title = "Burrito Order Form"
    return render_template("form.html", title=title)

@app.route("/submit", methods=["GET", "POST"])
def submit():
    tortilla = request.form.get("flexRadioDefault")
    rice = request.form.get("flexRadioDefault2")
    beans = request.form.get("flexRadioDefault3")
    protein = request.form.get("flexRadioDefault4")
    ingredients = request.form.getlist("inlineRadioOptions") 
    notes = request.form.get("notes") 
    first = request.form.get("first")
    last = request.form.get("last")
    title = "Thank you for your Order!"
    return render_template("submit.html", title=title, tortilla=tortilla, rice=rice, beans=beans, protein=protein, ingredients=ingredients, notes=notes, first=first, last=last)

if __name__ == "__main__":
    app.run()