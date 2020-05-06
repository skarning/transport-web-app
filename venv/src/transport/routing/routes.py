from flask import render_template, request, redirect, flash
from transport.forms.TransportationWorkerForm import TransportationWorkerForm
from transport.forms.TruckForm import TruckForm
from transport.forms.MissionForm import MissionForm
from transport import app
from transport.repositories.TransportationWorkerRepository import TransportationWorkerRepository
from transport.repositories.MissionRepository import MissionRepository
from transport.repositories.TruckRepository import TruckRepository
from transport.models.TransportationWorker import TransportationWorker
from transport.models.Truck import Truck
from transport.models.Mission import Mission


"""Redirects to home from the URL"""
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/missions")
def missions():
    mission_repos = MissionRepository()
    missions = mission_repos.get_all()

    return render_template("missions.html", missions=missions)


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


@app.route("/manage-logistics/add-truck",
           methods=["GET", "POST"])
def add_truck():
    form = TruckForm()
    if request.method == "POST" and form.validate_on_submit():

        truck_repos = TruckRepository()
        truck_repos.add(
            Truck(
                form.brand.data,
                form.type.data,
                form.registration_number.data
            )
        )
        flash("Truck added")

        return redirect(request.url)

    return render_template("add-truck.html", form=form)


@app.route("/manage-logistics/add-mission",
           methods=["GET", "POST"])
def add_mission():
    form = MissionForm()

    if request.method == "POST" and form.validate_on_submit():
        mission_repos = MissionRepository()
        mission_repos.add(
            Mission(
                form.postal_code.data,
                form.address.data,
                form.date.data,
                form.package_number.data,
                form.truck.data,
                form.transportation_worker.data
            )
        )

        flash("Mission added")

        return redirect(request.url)

    return render_template("add-mission.html", form=form)
