import json
import logging

import decimalencoder

from todoTable import updateItem


def update(event, context):
    data = json.loads(event['body'])
    if 'text' not in data or 'checked' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")

    # update the todo in the database
    result = updateItem(
        data['text'],
        event['pathParameters']['id'],
        data['checked']
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
