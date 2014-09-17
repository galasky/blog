from flask import Flask
app = Flask(__name__)

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/")
def route():
    return "Ya rien ici degage ! Cordialement."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
