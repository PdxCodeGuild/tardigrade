from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        temperature = 67
        nums = [1, 2, 3]
        return render_template('home.html', temperature = temperature, nums = nums)
    
    elif request.method == "POST":
        name_from_form = request.form["input_text"]
        print(name_from_form)
        return render_template('2home.html',name_from_form = name_from_form)



  
@app.route('/portfolio/')
def path2():
    return 'portfolio'

@app.route('/about/')
def path3():
    return 'about section'
    


app.run(debug=True)
