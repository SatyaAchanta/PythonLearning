# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

userJSON = '{"fName": "Satya", "lName":"Achanta", "age":28}'

# parse json to dict
user = json.loads(userJSON)

print(user['fName'])

# parse dict to json
playerDetails = {'name': 'Dravid', 'style': 'Right handed batsman', 'role': 'wicket keeper'}

playerDetailsJSON = json.dumps(playerDetails)

print(playerDetailsJSON)

