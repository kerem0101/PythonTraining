import json 

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

person_json=json.dumps(person,indent=4)
print(person_json)

with open('person.json', 'w') as f:
    json.dump(person, f, indent=4)

example= {}

with open('example.json','r') as file:
    example=json.load(file)

print(example)

class User:
    def __init__(self, name, age):
        self.name=name
        self.age=age

user = User('Max',27)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError(f"Object of type '{o.__class__.__name__}' is not JSON serializable")
    
userJson = json.dumps(user, default=encode_user)
print(userJson)

from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self,o)
    
userJson=json.dumps(user,cls=UserEncoder)
print(userJson)
userJson=UserEncoder().encode(user)
print(userJson)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJson, object_hook=decode_user)
print(type(user))
print(user.name)