
from flask import request, redirect
from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    my_name = "John"
    return f'Hello, {my_name}!'

@app.route('/hello')
def hello2():
    my_name = "Maciek "
    return f'Hello, {my_name}!'

@app.route('/blog', methods=['GET'])
def blog_main():
    return f"This is a main blog page"

@app.route('/blog/<id>')
def blog(id):
    return f"This is blog entry #{id}"


@app.route('/greeting', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("greeting.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")


@app.route("/warehouse_ugly")
def warehouse_ugly():
    items = ["screwdriver", "hammer", "saw"]
    html = "<ul>"
    for item in items:
        html = html + f"<li>{item}</li>"
    html += "</ul>"
    return html

@app.route("/warehouse")
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("greeting.html", items=items, errors=errors)



@app.route ('/greeting', methods=['GET', 'POST'])
def mypage():
   if request.method == 'GET':
       print("We received GET")
       return render_template("greeting.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")


@app.route ('/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("greeting.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return render_template("greeting.html")



