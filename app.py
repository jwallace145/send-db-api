from flask import Flask

import logging

from blueprints.routes import routes_blueprint
from blueprints.climbers import climbers_blueprint


def create_app():
    # create flask app
    app = Flask(__name__)

    # register blueprints
    app.register_blueprint(climbers_blueprint, url_prefix='/climbers')
    app.register_blueprint(routes_blueprint, url_prefix='/routes')

    return app


if __name__ == '__main__':
    app = create_app()

    app.run()
