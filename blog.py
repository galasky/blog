from flask import Flask
app = Flask(__name__)

@app.route("/blog")
def hello():
    return render_template("blog.html")

@app.route("/")
def hello():
    return "Ya rien ici dégage ! Cordialement."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
