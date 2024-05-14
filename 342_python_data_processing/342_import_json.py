import json
import requests

j_file = "data.json"

j_string = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}


with open(j_file) as json_file:
    data = json.load(json_file)
    print(data)
    print(type(data))
    print(data.keys())

    # JSON string -> loads() -> Python Dictionary Object
    # JSON file -> load() -> Python dictionary object
    # Python dictionary object -> dumps() -> JSON String
    # Python dicitonary object -> dump() -> JSON Object

    # https://sisayie.medium.com/working-with-json-and-python-a-cheatsheet-153a1d106e53

with open("json_test.json", "w") as write_file:
    json.dump(j_string, write_file)


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)