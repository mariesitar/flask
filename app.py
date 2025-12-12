from flask import Flask, render_template

app = Flask(__name__)

# Home Page Route
@app.route("/")
def home():
    return render_template("index.html")

# About Page Route
@app.route("/about")
def about_page():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)