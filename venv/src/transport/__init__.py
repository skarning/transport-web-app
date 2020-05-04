from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""Bootstrap navigation bar"""
nav = Nav()
nav.init_app(app)


Bootstrap(app)

"""
Imports after app adn nav initialization because of
circular dependency with routes,confguration and navigation
"""
from transport.confgurations import configuration
db = SQLAlchemy(app)
from transport.routing import navigation
from transport.models.Mission import Mission
from transport.models.TransportationWorker import TransportationWorker
from transport.models.Truck import Truck
from transport.routing import routes
