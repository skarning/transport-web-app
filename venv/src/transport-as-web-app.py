from flask import Flask, render_template, request, redirect

app = Flask(__name__)


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
    if request.method == "POST":
        print(request.form)
        return redirect(request.url)

    return render_template("add-transportation-worker.html")


if __name__ == "__main__":
    app.run()
