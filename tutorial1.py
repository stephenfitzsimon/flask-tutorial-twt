from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#can pass a parameter to render in the template
@app.route("/") #use a decorator to note root folder for the project
def home():
    # make a home page
    # render_template looks in the template folder to produce the html
    # note that the folder must be called template!
    #recall that {{}} will be replaced with the parameter
    return render_template("index.html", content = ["tim", "joe", "bill"])



# # tag the parameter for the function in the decorator
# # so that the parameter can be passed by the URL
# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}"

# # make an admin page and redirect users who do not have
# # credentials
# @app.route("/admin")
# def admin():
#     # send them to the hello user page, but pass admin as the
#     return redirect(url_for("user", name="Admin"))

if __name__ == "__main__":
    app.run()