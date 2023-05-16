# User database management application

## Installation

To install this application, you can clone this repository and install the required dependencies by running the following command:

```
pip install -r requirements.txt
```
---

## Usage

First you need to connect your application to the MongoDB database by pasting [Connection String URI Format](https://www.mongodb.com/docs/manual/reference/connection-string/) in project/main.py. Make sure you name the database "UsersDB" and create a collection "users"
```
db = Database(" ", "UsersDB", "users")
```
To run the tests, repeat the previous step by pasting the new Connection String URI Format into project/tests.py and name the database: "Users_DB" and collection: "users"

``` class TestDatabase(unittest.TestCase):
    def setUp(self):
        #Mongodb link
        self.uri = " "
        self.database_name = "UsersDB_test"
        self.collection_name = "users" 
```
---


To use this application, run the following command in terminal:

```
python project/main.py
```

This will launch the application and display a menu with several options:

1. save user data
2. show user data
3. delete user data
4. edit user data
5. search for users
6. close the program

To select an option, enter the corresponding number and press Enter. Follow the instructions to enter the required information and the application will perform the desired action.

## Credits

This application was created by Mikolaj Jagielak / jagiel02.
