from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    headline = "headline"
    return render_template( "index.html",headline = headline)


@app.route("/more", methods = ["POST"])
def more():
    name = request.form.get("name")
    return render_template("more.html",name= name)

