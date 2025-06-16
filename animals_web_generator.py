import json
from tkinter.font import names


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

import json

# Open and read the JSON file
with open("animals_data.json", "r") as file:
    animals = json.load(file)

# Loop through each animal
for animal in animals:
    print()

    # Print the name if it exists
    name = animal.get("name")
    if name:
        print(f"Name: {name}")

    # Print the diet if it exists in 'characteristics'
    diet = animal.get("characteristics", {}).get("diet")
    if diet:
        print(f"Diet: {diet}")

    # Print the first location if the list exists and is not empty
    locations = animal.get("locations")
    if locations and len(locations) > 0:
        print(f"Location: {locations[0]}")

    # Print the type if it exists in 'characteristics'
    animal_type = animal.get("characteristics", {}).get("type")
    if animal_type:
        print(f"Type: {animal_type}")