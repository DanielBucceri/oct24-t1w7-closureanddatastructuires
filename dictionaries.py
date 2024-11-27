# List - ordered (indexed) collectioin of items - mutable - can have duplicates

# Dictionary (dict) - collection of items - mutable - unordered - not idnexed instead key: 
# keyed - key.value pairs - the key cannot be a duplicate in the dict. 

person1 = {
    "name": "Donkey",
    "age": 456,
    "last_name": "Ponkey"
}


print(person1["name"])
print(person1.get("foof", "you tripping"))
# print(person1["fsff"])

person1["address"] = {'state': "NSW", "City": "Sydney","postcode": "2000"}# add to dict. overwrite if key already there
print(person1["address"]["state"]) # print out key in dictionairy  within dictinary

#loop
for key, val in person1.items():
    print(f"key:{key}")
    print(f"Value: {person1[key]}")
