from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/") #use a decorator to note root folder for the project
def home():
    # make a home page
    return "<h1>Hello world</h1> <p>And here is some paragraph tagged text</p>"

# tag the parameter for the function in the decorator
# so that the parameter can be passed by the URL
@app.route("/<name>")
def user(name):
    return f"Hello {name}"

# make an admin page and redirect users who do not have
# credentials
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()