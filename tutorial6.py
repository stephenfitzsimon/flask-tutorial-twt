from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
#needed to encrypt the session
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=2)

#can pass a parameter to render in the template
@app.route("/") #use a decorator to note root folder for the project
def home():
    return render_template("index.html", content = "Testing")

@app.route("/login", methods = ["POST", "GET"]) 
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login successful")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in.")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"{user} has been logged out successfully.", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user = user)
    else:
        flash("No user logged in")
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)