# from pprint import pprint
import unittest
import boto3
from moto import mock_dynamodb2
import sys
import warnings
sys.path.insert(1, '../todos/')


@mock_dynamodb2
class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings(
            "ignore",
            category=ResourceWarning,
            message="unclosed.*<socket.socket.*>"
        )
        warnings.filterwarnings(
            "ignore",
            category=DeprecationWarning,
            message="callable is None.*"
        )
        warnings.filterwarnings(
            "ignore",
            category=DeprecationWarning,
            message="Using or importing.*"
        )

        """Create the mock database and table"""
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.uuid = "123e4567-e89b-12d3-a456-426614174000"
        self.text = "Aprender DevOps y Cloud en la UNIR"

        from ToDoCreateTable import create_todo_table
        self.table = create_todo_table(self.dynamodb)

    def tearDown(self):
        """Delete mock database and table after test is run"""
        self.table.delete()
        self.dynamodb = None

    def test_table_exists(self):
        self.assertTrue(self.table)  # check if we got a result

    def test_list_todo(self):
        from todoTable import createItem
        from todoTable import getAll

        # Testing file functions
        # Table mock
        createItem(self.text, self.uuid)
        self.assertEqual(200, getAll()['ResponseMetadata']['HTTPStatusCode'])

    def test_put_todo(self):
        from todoTable import createItem

        result = createItem(self.text, self.uuid)
        self.assertEqual(self.uuid, result['id'])

    def test_put_todo_error(self):
        from todoTable import createItem

        self.assertRaises(Exception, createItem("", self.uuid))
        self.assertRaises(Exception, createItem("", ""))
        self.assertRaises(Exception, createItem(self.text, ""))

    def test_get_todo(self):
        from todoTable import createItem
        from todoTable import getItem

        createItem(self.text, self.uuid)
        self.assertEqual(
            200,
            getItem(self.uuid)['ResponseMetadata']['HTTPStatusCode']
        )
        self.assertEqual(self.text, getItem(self.uuid)['Item']['text'])

    def test_get_todo_error(self):
        from todoTable import createItem
        from todoTable import getItem

        createItem(self.text, self.uuid)
        self.assertRaises(TypeError, getItem(""))

    def test_update_todo(self):
        from todoTable import updateItem
        from todoTable import createItem
        from todoTable import getItem
        updated_text = "Aprender más cosas que DevOps y Cloud en la UNIR"

        createItem(self.text, self.uuid)
        self.assertEqual(
            200,
            updateItem(
                updated_text,
                self.uuid,
                "false"
            )['ResponseMetadata']['HTTPStatusCode']
        )
        self.assertEqual(updated_text, getItem(self.uuid)['Item']['text'])

    def test_update_todo_error(self):
        from todoTable import updateItem
        from todoTable import createItem
        updated_text = "Aprender más cosas que DevOps y Cloud en la UNIR"

        createItem(self.text, self.uuid)
        self.assertRaises(Exception, updateItem(updated_text, "", "false"))
        self.assertRaises(TypeError, updateItem("", self.uuid, "false"))
        self.assertRaises(Exception, updateItem(updated_text, self.uuid, ""))

    def test_delete_todo(self):
        from todoTable import deleteItem
        from todoTable import createItem

        createItem(self.text, self.uuid)
        self.assertEqual(
            200,
            deleteItem(self.uuid)['ResponseMetadata']['HTTPStatusCode']
        )

    def test_translate_todo(self):
        from todoTable import getTranslate
        from todoTable import createItem
        createItem(self.text, self.uuid)

        self.assertEqual(
            200,
            getTranslate(self.uuid, 'fr')['ResponseMetadata']['HTTPStatusCode']
        )

        self.assertEqual(
            self.uuid,
            getTranslate(self.uuid, 'fr')['Item']['id']
        )


if __name__ == '__main__':
    unittest.main()
