import json
import logging
import uuid

import decimalencoder

from todoTable import createItem


def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")

    result = createItem(
        text=data['text'],
        id=str(uuid.uuid1())
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result, cls=decimalencoder.DecimalEncoder)
    }

    return response
