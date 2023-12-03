import json

# with open("person.json") as file:
#     data = json.load(file)

data = """

    {
        "firstName":"parzival",
        "lastName":"dinc",
        "hobbies": ["oyun","sinema"],
        "age":23,
        "children": [
            {
                "firstName": "knauc",
                "age":3
            }
        ]
    }

    """

data = json.loads(data)
print(data)    
print(type(data))
print(data["firstName"])