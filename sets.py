# List - ordered (indexed) collectioin of items - mutable - can have duplicates

# Set - unordered - Not indexed - mutable - cnnot have duplicates.

names_set = {"John","Mike","Daniel","Donkey"}

print(names_set)
print(type(names_set))

names_set.add('New Addition')
print(names_set)

names_set.remove('John')
names_set.add('Mike')
print(names_set)

