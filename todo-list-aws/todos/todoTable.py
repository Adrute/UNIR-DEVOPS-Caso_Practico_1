import boto3
from botocore.exceptions import ClientError
import time
import os

# Pruebas en local
# dynamodb = boto3.resource('dynamodb',
#    endpoint_url='http://172.18.0.1:8000')

# Pruebas AWS
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])


# Devuelve todos los registros de la tabla
def getAll():
    try:
        response = table.scan()
    except ClientError as e:
        print("Error >> scan_todo")
        print(e.response['Error']['Message'])
    else:
        return response


# Creamos un registro en la tabla
def createItem(text, id=None):
    timestamp = str(time.time())

    item = {
        'id': id,
        'text': text,
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    try:
        table.put_item(Item=item)
    except ClientError as e:
        print("Error >> put_todo")
        print(e.response['Error']['Message'])
    else:
        return item


# Actualiza el registro según el id indicado
def updateItem(text, id, checked):
    timestamp = str(time.time())

    try:
        response = table.update_item(
            Key={
                'id': id
            },
            ExpressionAttributeNames={
                '#todo_text': 'text',
            },
            ExpressionAttributeValues={
                ':text': text,
                ':checked': checked,
                ':updatedAt': timestamp,
            },
            UpdateExpression='SET #todo_text = :text, '
                             'checked = :checked, '
                             'updatedAt = :updatedAt',
            ReturnValues='ALL_NEW'
        )

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response


# Obtiene la traducción del texto de la propiedad "text" según el id indicado
def getTranslate(id, lang):
    apitranslate = boto3.client('translate')

    try:
        response = table.get_item(
            Key={
                'id': id
            }
        )
        text = response['Item']['text']
        translatedText = apitranslate.translate_text(
            Text=text,
            SourceLanguageCode='auto',
            TargetLanguageCode=lang
        )

        response['Item']['text'] = translatedText['TranslatedText']
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response


# Obtiene un registro según el id indicado
def getItem(id):
    try:
        response = table.get_item(
            Key={
                'id': id
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response


def deleteItem(id):

    try:
        response = table.delete_item(
            Key={
                'id': id
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response
