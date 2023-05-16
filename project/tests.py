import unittest
from pymongo import MongoClient
from app.config import save_user_data, edit_user
from app.config import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        #Mongodb linkt
        self.uri = " "
        self.database_name = "UsersDB_test"
        self.collection_name = "users"
        self.db = Database(self.uri, self.database_name, self.collection_name)
        self.client = MongoClient(self.uri)
        self.test_db = self.client.get_database(self.database_name)
        self.test_collection = self.test_db[self.collection_name]

    def test_save_user_data(self):
        save_user_data(self.db, "Mikolaj", "Jagielak", "Warsaw", "PL")
        result = self.test_collection.find_one({"user.name": "Mikolaj", "user.last_name": "Jagielak"})
        self.assertEqual(result["address"]["city"], "Warsaw")
        self.assertEqual(result["address"]["country"], "PL")

    def test_edit_user(self):
        save_user_data(self.db, "Mikolaj", "Jagielak", "Warsaw", "PL")

        edit_user(self.db, "Mikolaj", "Jagielak", 1, "Rafal")
        result = self.test_collection.find_one({"user.name": "Rafal", "user.last_name": "Jagielak"})
        self.assertEqual(result["user"]["name"], "Rafal")

        edit_user(self.db, "Rafal", "Jagielak", 2, "Siekiera")
        result = self.test_collection.find_one({"user.name": "Rafal", "user.last_name": "Siekiera"})
        self.assertEqual(result["user"]["last_name"], "Siekiera")

    def test_delete_user(self):
        save_user_data(self.db, "Mikolaj", "Jagielak", "Warsaw", "PL")

        self.db.delete_user("Mikolaj", "Jagielak")
        result = self.test_collection.find_one({"user.name": "Mikolaj", "user.last_name": "Jagielak"})
        self.assertIsNone(result)

    def test_find_user(self):
        save_user_data(self.db, "Mikolaj", "Jagielak", "Warsaw", "PL")
        result = self.db.find_user("Mikolaj", "Jagielak")
        self.assertEqual(result["user"]["name"], "Mikolaj")
        self.assertEqual(result["user"]["last_name"], "Jagielak")

    def tearDown(self):
        self.test_collection.delete_many({})


if __name__ == '__main__':
    unittest.main()
