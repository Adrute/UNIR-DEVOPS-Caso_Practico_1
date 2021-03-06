import json

import decimalencoder

from todoTable import getItem


def get(event, context):

    result = getItem(
        event['pathParameters']['id']
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
