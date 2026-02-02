# Dictionaries

sample_of_dictionaries = {
    "tao": "emong",
    "hayop": "si doggy",
    "halaman": "KA ULIT"
}

for key, values in sample_of_dictionaries.items():
    print(key, values)


# Nested Dictionaries

travel_log = {
    "France" : ["Paris", "Lilie", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"],
    "Philippines" : ["Manila", "Makati", "BGC"]
}

print(travel_log["France"][1])


# Printint the nested List
letters = ['a', 'b', ['c', 'd']]
print(letters[2][1])

# nested dict consist of dict and list
travel_logs = {
    "France" : {
            "location" : ["Paris", "Lilie", "Dijon"],
            "total_visits" : 1
        },

    "Germany" : {
           "location" : ["Haamburg", "Stuttgart", "Berlin"],
           "total_visits" : 1
        },
    "Philippines" : {
            "location" : ["Manila", "Makati", "BGC"],
            "total_visit" : 2
        }
}

# try to print the "Stuttgart"
my_destination = travel_logs["Germany"]["location"][1]
print(my_destination)