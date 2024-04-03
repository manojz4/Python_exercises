import json

# The json.load() function reads a JSON file and parses it into a Python dictionary.
with open(r'/home/dhpcsa/person.json', "r") as fh:
    data = json.load(fh)
    
print(data)    



# The json.dump() method directly writes a Python dictionary to a file in JSON format.
# with open('person_copy.json', "w") as outfile:
#     json.dump(data, outfile)