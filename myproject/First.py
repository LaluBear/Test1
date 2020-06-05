from Flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    name = "david"
    return render_template("hello.html", name=f"Hello, {name}!")
