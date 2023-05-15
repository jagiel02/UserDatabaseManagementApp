from pydantic import BaseModel, validator
from dataclasses import dataclass
import json

@dataclass()
class Address():
    city: str
    country: str

    @validator('city', 'country')
    def cant_contain_space(cls, v):
        if ' ' in v:
            raise ValueError('must not contain a space')
        return v.title()
@dataclass()
class User():
    name: str
    last_name : str

    @validator('name', 'last_name')
    def cant_contain_space(cls, v):
        if ' ' in v:
            raise ValueError('must not contain a space')
        return v.title()


class Config(BaseModel):
    user : User
    address : Address

    def __post_init__(self):
        self.json_encoders = {
            User: f'{self.user.name} {self.user.last_name}', 
            Address: f'{self.address.city} {self.address.country}'
        }

def get_json_data():
    with open('app/data.json', 'r') as file:
        data = json.load(file)
    return data


def save_user_data():
    user_name = input('Enter your name: ')
    user_last_name = input('Enter your last name: ')
    user_city = input('Enter your city: ')
    user_country = input('Enter your country: ')

    user = Config(user=User(name=user_name, last_name=user_last_name),
                  address=Address(city=user_city, country=user_country))
    
    with open('app/data.json', 'a', newline='') as file:
            json_data = user.json(by_alias=True)
            json_object = json.loads(json_data)
            json.dump(json_object, file, sort_keys=True, indent=6)
            

def delete_user_data(name, last_name):
    
    data = get_json_data()

    for user in data:
        if user['user']['name'] == name.title() and user['user']['last_name'] == last_name.title():
            data.remove(user)
            print(f'Removed user: {name} {last_name}')
            break
    else:
        print(f'User {name} {last_name} not found')

    with open('app/data.json', 'w') as file:
        json.dump(data, file, sort_keys=True, indent=6)

