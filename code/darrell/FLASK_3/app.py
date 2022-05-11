from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/order/', methods=["GET", "POST"])
def order():
    if request.method == "GET":
        return render_template('order.html')
    elif request.method == "POST":
        checks = request.form.getlist('check')
        print('checkboxes', checks)
        return render_template('order_confirmation.html', checks=checks)


@app.route('/checkout/')
def checkout():
    return render_template('checkout.html')


app.run(debug=True)
