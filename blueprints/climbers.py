from flask import Blueprint
from flask import request

from clients.dynamodb_client import dynamodb_client
from models.climber.climber import Climber

climbers_blueprint = Blueprint('climbers_blueprint', __name__)


@climbers_blueprint.route('/health', methods=['GET'])
def get_health():
    """ Get health of Climbers API """

    return {'healthy': True}


@climbers_blueprint.route('/insert', methods=['POST'])
def insert_climber():

    # create climber from request formdata
    climber = Climber(**request.form)

    # insert climber into dynamodb table
    dynamodb_client.put_item(
        table='climbers',
        item=climber
    )

    return {'successful': True}
