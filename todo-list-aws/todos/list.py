import json

import decimalencoder
from todoTable import getAll


def list(event, context):
    result = getAll()

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
