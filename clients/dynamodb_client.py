import boto3
import datetime
import random
import sys

from models.route.route import Route


class DynamoDBClient:

    def __init__(self, region: str) -> None:
        """ DynamoDB Client Constructor. """
        self.region = region

        # create dynamo db client
        self.client = boto3.client('dynamodb', region_name=region)

    def put_item(self, table: str, item: object) -> None:

        # initialize item
        item_dict = {}

        # generate unique identifier
        identifier = str(datetime.datetime.utcnow()) + 'T' + \
            str(random.randint(0, sys.maxsize))

        item_dict['id'] = {
            'S': identifier
        }

        for key, value in vars(item).items():
            item_dict[key] = {
                'S': value
            }

        response = self.client.put_item(
            TableName=table,
            Item=item_dict
        )

        print(response)
        return(response)

    def put_route(self, table: str, route: Route) -> None:

        # generate unique identifier
        route_id = str(datetime.datetime.utcnow()) + 'T' + \
            str(random.randint(0, sys.maxsize))

        response = self.client.put_item(
            TableName=table,
            Item={
                'id': {
                    'S': route_id
                },
                'name': {
                    'S': route.name
                },
                'grade': {
                    'S': route.grade
                },
                'climb_type': {
                    'S': route.climb_type
                },
                'wall': {
                    'S': route.wall
                },
                'crag': {
                    'S': route.crag
                },
                'style': {
                    'S': route.style
                },
                'ascent': {
                    'S': route.ascent
                },
                'height': {
                    'N': route.height
                },
                'pitches': {
                    'N': route.pitches,
                },
                'timestamp': {
                    'S': str(route.timestamp)
                }
            }
        )
        print(response)
        return response


dynamodb_client = DynamoDBClient(region='us-east-1')
