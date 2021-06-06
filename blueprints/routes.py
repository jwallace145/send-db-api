from flask import Blueprint, request

from models.route.route import Route

from services.clients import dynamodb_client
from clients.logging_client import get_logger


routes_blueprint = Blueprint('routes_blueprint', __name__)

logger = get_logger(__name__)


@routes_blueprint.route('/health', methods=['GET'])
def get_health():
    """ Get health of Routes API """

    logger.info('Routes API is healthy')

    return {'healthy': 'true'}


@routes_blueprint.route('/insert', methods=['POST'])
def insert_route():
    """ Insert Route. """

    # create route
    route = Route(**request.form)

    # insert route into dynamo db table
    response = dynamodb_client.put_route(route)

    return {'successful': True}


@routes_blueprint.route('/delete', methods=['DELETE'])
def delete_route():

    response = dynamodb_client.delete_route(**request.form)

    return {'successful': True}
