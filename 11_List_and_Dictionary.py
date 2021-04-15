grades = [1, 2, 3, 4, 5]
city_names_list = ["Ljubljana", "Maribor", "New York", "London"]

# for city_name_string in city_names_list:
    # print(city_name_string)

# print(grades[4])

capital_of_slovenia = {
    "name": "Ljubljana",
    "population": 200000,
    "crime_rate": "low",
    "is_clean": True
}

for item in capital_of_slovenia.items():
    # (key, value)[1]
    print(f"The {item[0]} is {item[1]}.")

# print(capital_of_slovenia["name"])
# print(capital_of_slovenia.get("population"))

capital_of_england = {
    "name": "London",
    "population": 10000000,
    "crime_rate": "moderate",
    "is_clean": False,
    "suburbs": ["Center", "Yoho", "The Bridge"],
    "major": {
        "name": "Queen Elizabeth",
        "title": "queen"
    }
}

capitals = [capital_of_slovenia, capital_of_england]

# print(capitals[1].get("crime_rate"))
# print(capitals[1]["is_clean"])
# print(capitals[1]["suburbs"])

my_book = {
    "title": "Kako izgoreti",
    "pages": 200,
    "author": "Nekdo"
}

my_fruit = {
    "type": "apple",
    "color": "red",
    "weight": 100
}
