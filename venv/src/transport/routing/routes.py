from flask import render_template, request, redirect, flash
from transport.forms.TransportationWorkerForm import TransportationWorkerForm
from transport import app
from transport.repositories.TransportationWorkerRepository import TransportationWorkerRepository
from transport.models.TransportationWorker import TransportationWorker


"""Redirects to home from the URL"""
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
        trans_wor_repos = TransportationWorkerRepository()
        trans_wor_repos.add(
            TransportationWorker(
                form.full_name.data, form.birthday.data,
                form.email.data, form.job_title.data, form.phone_number.data
                )
            )

        flash("Transportation-worker added")

        return redirect(request.url)

    return render_template("add-transportation-worker.html", form=form)
