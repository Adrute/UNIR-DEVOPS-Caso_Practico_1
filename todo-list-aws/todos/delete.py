from todoTable import deleteItem


def delete(event, context):
    # delete the todo from the database
    deleteItem(
        event['pathParameters']['id']
    )

    # create a response
    response = {
        "statusCode": 200
    }

    return response
