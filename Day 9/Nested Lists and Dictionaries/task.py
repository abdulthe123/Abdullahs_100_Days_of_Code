capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }


nested_list = ["A", "B", ["C", "D"]]

travel_log = {
    "France": {
        "numTimesVisited": 12,
        "citiesVisited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "citiesVisited": ["Stuttgart", "Berlin"],
        "numTimesVisited": 5
    },
}

print(travel_log["Germany"]["citiesVisited"][0])