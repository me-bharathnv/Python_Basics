people = [
    {"name":"Bharath", "city":"kunigal"},
    {"name":"ravish", "city":"magadi"},
    {"name":"naveen", "city":"nelamangala"}
]



people.sort(key= lambda person: person["name"])

print(people)