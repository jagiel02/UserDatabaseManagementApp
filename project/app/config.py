from typing import Dict
from dataclasses import dataclass, asdict
from bson import ObjectId
from pymongo import MongoClient


class Database:
    def __init__(self, uri: str, database_name: str, collection_name: str):
        self.client = MongoClient(uri)
        self.db = self.client.get_database(database_name)
        self.collection = self.db[collection_name]

    def insert_user(self, user_dict: Dict):
        user_dict["_id"] = ObjectId()
        self.collection.insert_one(user_dict)

    def delete_user(self, user_name: str, user_lname: str):
        result = self.collection.delete_one({"user.name": user_name, "user.last_name": user_lname})
        if result.deleted_count == 1:
            print(f"User {user_name} {user_lname} has been deleted.")
        else:
            print("User not found.")

    def all_data_return(self):
        count = 0
        for i in self.collection.find({}, {'_id': 0}):
            print(i)
            count += 1
        return print("Total amount of users: ", count)

    def find_user(self, user_name: str, user_lname: str):
        result = self.collection.find_one({"user.name": user_name, "user.last_name": user_lname})
        print(self.collection.find_one({"user.name": user_name, "user.last_name": user_lname}, {'_id': 0}))
        return result

    def update_user(self, user_id: ObjectId, new_values: dict):
        self.collection.update_one({"_id": user_id}, new_values)


@dataclass()
class Address:
    city: str
    country: str

    def to_dict(self):
        return asdict(self)


@dataclass()
class User:
    name: str
    last_name: str

    def to_dict(self):
        return asdict(self)


@dataclass()
class Config:
    user: User
    address: Address

    def to_dict(self):
        return {"user": self.user.to_dict(), "address": self.address.to_dict()}


def save_user_data(db: Database, user_name: str, user_lname: str, user_city: str, user_country: str):
    user = Config(user=User(name=user_name, last_name=user_lname),
                  address=Address(city=user_city, country=user_country))

    db.insert_user(user.to_dict())


def edit_user(db: Database, user_name: str, user_lname: str, choose_option: int, new_value: str):
    user = db.find_user(user_name, user_lname)

    if not user:
        print("User does not exist")
        return

    if choose_option == 1:
        new_name = new_value
        new_values = {"$set": {"user.name": new_name}}
        db.update_user(user["_id"], new_values)
        updated_user = db.find_user(new_name, user_lname)
        print(f"You have just updated {user} to {updated_user}")

    elif choose_option == 2:
        new_lname = new_value
        new_values = {"$set": {"user.last_name": new_lname}}
        db.update_user(user["_id"], new_values)
        updated_user = db.find_user(user_name, new_lname)
        print(f"You have just updated {user} to {updated_user}")

    elif choose_option == 3:
        new_city = new_value
        new_values = {"$set": {"address.city": new_city}}
        db.update_user(user["_id"], new_values)
        updated_city = db.find_user(user_name, user_lname)
        print(f"You have just updated {user} to {updated_city}")

    elif choose_option == 4:
        new_country = new_value
        new_values = {"$set": {"address.country": new_country}}
        db.update_user(user["_id"], new_values)
        updated_country = db.find_user(user_name, user_lname)
        print(f"You have just updated {user} to {updated_country}")





