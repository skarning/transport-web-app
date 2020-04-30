from flask import Flask, render_template, request, redirect, flash
from forms.TransportationWorkerForm import TransportationWorkerForm
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "!SSG¤#269&vcd2%#"
nav = Nav()
nav.init_app(app)


@nav.navigation()
def navigation_bar():
    return Navbar(
        View("Home", "home"),
        View("Missions", "missions"),
        Subgroup(
            "Add",
            View("Add transportation-worker", "add_transportation_worker")
        )
    )


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/missions")
def missions():
    return render_template("missions.html")


@app.route("/manage-logistics/add-transportation-worker",
           methods=["GET", "POST"])
def add_transportation_worker():
    form = TransportationWorkerForm()
    if request.method == "POST" and form.validate_on_submit():
        # Create new Object and post to database
        flash("Transportation-worker added")
        return redirect(request.url)

    return render_template("add-transportation-worker.html", form=form)


if __name__ == "__main__":
    app.run()
