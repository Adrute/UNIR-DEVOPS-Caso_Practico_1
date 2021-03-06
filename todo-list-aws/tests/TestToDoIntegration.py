import os
from unittest import TestCase

import requests


class TestToDoIntegration(TestCase):
    apiEndpoint: str

    @classmethod
    def setUp(self) -> None:
        envId = os.environ['ENV_ID']
        protocol = 'https://'
        path = ".execute-api.us-east-1.amazonaws.com/Stage/todos"
        self.apiEndpoint = protocol + envId + path
        self.itemId = ''

    def test_complete_api_flow(self):
        print('##### a.- Creamos el registro #####')
        createBody = '{ "text": "Aprender Serverless" }'

        createResponse = requests.post(self.apiEndpoint, createBody)
        itemId = createResponse.json()['id']
        self.assertEqual(200, createResponse.status_code)

        # -------------------------
        print('##### b.- Obtenemos una lista de todos los elementos #####')

        getAllResponse = requests.get(self.apiEndpoint)

        self.assertEqual(200, getAllResponse.status_code)

        # Revisamos que el total obtenido no sea 0
        self.assertIsNot(0, len(getAllResponse.json()))

        # -------------------------
        print('##### c.- Obtenemos el registro del item creado #####')

        getItemPath = self.apiEndpoint + '/' + itemId
        getItemResponse = requests.get(getItemPath)

        self.assertEqual(200, getItemResponse.status_code)

        # Comparamos la respuesta actual con la de creación
        self.assertEqual(getItemResponse.json(), createResponse.json())

        # -------------------------
        print('##### d.- Modificamos el registro #####')
        updateBody = '{ "text": "Learn python and more", "checked": true }'

        updatePath = self.apiEndpoint + '/' + itemId
        updateResponse = requests.put(updatePath, updateBody)

        # Obtenemos de nuevo el item para comprobar que se ha actualizado
        getNewValueItem = requests.get(getItemPath)

        self.assertEqual(200, updateResponse.status_code)
        self.assertEqual(getNewValueItem.json(), updateResponse.json())
        self.assertEqual(
            'Learn python and more',
            getNewValueItem.json()['text']
        )

        # -------------------------
        print('##### e.- Borramos el registro generado #####')

        deletePath = self.apiEndpoint + '/' + itemId
        deleteResponse = requests.delete(deletePath)

        self.assertEqual(200, deleteResponse.status_code)

        # Obtenemos el item para comprobar que no existe
        getDeletedItemResponse = requests.get(getItemPath)
        self.assertNotEqual(200, getDeletedItemResponse.status_code)
