from flask import Blueprint
from flask import request

from clients.dynamodb_client import dynamodb_client
from models.route.route import Route

routes_blueprint = Blueprint('routes_blueprint', __name__)


@routes_blueprint.route('/health', methods=['GET'])
def get_health():
    """ Get healht of Routes API """

    return {'healthy': 'true'}


@routes_blueprint.route('/insert', methods=['POST'])
def insert_route():

    # create route
    route = Route(
        name=request.form['name'],
        grade=request.form['grade'],
        climb_type=request.form['climb_type'],
        wall=request.form['wall'],
        crag=request.form['crag'],
        style=request.form['style'],
        ascent=request.form['ascent'],
        height=request.form['height'],
        pitches=request.form['pitches'],
        timestamp=request.form['timestamp']
    )

    # insert route into dynamo db table
    response = dynamodb_client.put_route(
        table='Routes',
        route=route
    )

    print(response)

    return {'healthy': 'true'}
