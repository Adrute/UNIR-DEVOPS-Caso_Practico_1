import json

import boto3
import decimalencoder

from todoTable import getTranslate

comprehend = boto3.client('comprehend')


def translate(event, context):

    result = getTranslate(
        event['pathParameters']['id'],
        event['pathParameters']['lang']
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
