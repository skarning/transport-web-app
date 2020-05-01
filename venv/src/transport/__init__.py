from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""
Bootstrap navigation bar
"""
nav = Nav()
nav.init_app(app)

"""
Imports after app adn nav initialization because of
circular dependency with routes,confguration and navigation
"""
from transport.routing import routes
from transport.confgurations import configuration
from transport.routing import navigation

"""
Activating libs
"""
db = SQLAlchemy(app)
Bootstrap(app)
