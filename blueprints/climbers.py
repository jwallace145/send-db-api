from flask import Blueprint, request

from models.climber.climber import Climber

from services.clients import dynamodb_client
from clients.logging_client import get_logger

climbers_blueprint = Blueprint('climbers_blueprint', __name__)

logger = get_logger(__name__)


@climbers_blueprint.route('/health', methods=['GET'])
def get_health():
    """ Get health of Climbers API """

    logger.info('Climbers API is healthy')

    return {'healthy': True}


@climbers_blueprint.route('/insert', methods=['POST'])
def insert_climber():

    # create climber from request formdata
    climber = Climber(**request.form)

    logger.info('insert climber')

    # insert climber into dynamodb table
    dynamodb_client.put_climber(climber)

    return {'successful': True}


@climbers_blueprint.route('/delete', methods=['DELETE'])
def delete_climber():

    response = dynamodb_client.delete_climber(**request.form)

    return {'successful': True}
