from app.config import save_user_data, edit_user
from app.config import Database
db = Database(" ", "UsersDB", "users")
if __name__ == '__main__':
    while True:
        print("Choose an option:")
        print("1. Save user data")
        print("2. Show user data")
        print("3. Delete user data")
        print("4. Edit user data")
        print("5. Search for users")
        print("6. Close program")

        option = input("Enter option number: ")

        if option == "1":
            user_name = input("Enter your name: ")
            user_lname = input("Enter your last name: ")
            user_city = input("Enter your city: ")
            user_country = input("Enter your country: ")
            save_user_data(db, user_name, user_lname, user_city, user_country)
            print("User data saved successfully!")

        if option == "2":
            db.all_data_return()

        if option == "3":
            user_name = input("Enter name: ")
            user_lname = input("Enter last name: ")
            db.delete_user(user_name, user_lname)

        if option == "4":
            user_name = input('Enter user name you want to edit')
            user_lname = input('Enter user last name you want to edit')
            choose_option = int(input('Choose what you want to edit: 1. name, 2. last name, 3. city, 4. country'))
            new_value = input('Enter new value')
            edit_user(db, user_name, user_lname, choose_option, new_value)

        if option == "5":
            user_name = input("Enter user name")
            user_lname = input("Enter user last name")
            db.find_user(user_name, user_lname)

        if option == "6":
            break
 
