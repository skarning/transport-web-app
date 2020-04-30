from flask import Flask, render_template, request, redirect
from forms.TransportationWorkerForm import TransportationWorkerForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "!SSG¤#269"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/missions")
def missions():
    return render_template("missions.html")


@app.route("/manage-logistics")
def manage_logistics():
    return render_template("manage-logistics.html")


@app.route("/manage-logistics/add-transportation-worker",
           methods=["GET", "POST"])
def add_transportation_worker():
    form = TransportationWorkerForm()
    if request.method == "POST" and form.validate_on_submit():
        # Create new Object and post to database
        return redirect(request.url)

    return render_template("add-transportation-worker.html", form=form)


if __name__ == "__main__":
    app.run()
