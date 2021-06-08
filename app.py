
from flask import request, redirect
from flask import render_template
from flask import Flask

app = Flask(__name__)




@app.route('/tata', methods=['GET', 'POST'])
def tata():
   if request.method == 'GET':
       print("We received GET")
       return render_template("parent.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")




@app.route ('/mypage/me', methods=['GET', 'POST'])
def mypage():
   if request.method == 'GET':
       print("We received GET")
       return render_template("me.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")


@app.route ('/mypage/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return render_template("contact.html")

