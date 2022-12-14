from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#can pass a parameter to render in the template
@app.route("/") #use a decorator to note root folder for the project
def home():
    return render_template("index.html", content = "Testing")

@app.route("/test") 
def test():
    return render_template("new.html")

if __name__ == "__main__":
    app.run(debug = True)