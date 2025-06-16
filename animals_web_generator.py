import json

# Step 1: Load the animal data from the JSON file
with open("animals_data.json", "r", encoding="utf-8") as file:
    animals = json.load(file)

# Step 2: Create an empty string to collect HTML content
output = ""

# Step 3: Loop through each animal in the data list
for animal in animals:
    # Get the name of the animal
    name = animal.get("name")

    # Get the diet from the characteristics
    diet = animal.get("characteristics", {}).get("diet")

    # Get the first location (if available)
    locations = animal.get("locations")
    location = locations[0] if locations else None

    # Get the type from the characteristics
    animal_type = animal.get("characteristics", {}).get("type")

    # Start a new list item with the correct class
    output += '<li class="cards__item">\n'

    # Add animal details (only if the data exists)
    if name:
        output += f"Name: {name}<br/>\n"
    if diet:
        output += f"Diet: {diet}<br/>\n"
    if location:
        output += f"Location: {location}<br/>\n"
    if animal_type:
        output += f"Type: {animal_type}<br/>\n"

    # Close the list item
    output += "</li>\n"

# Step 4: Read the HTML template file
with open("animals_template.html", "r", encoding="utf-8") as file:
    template = file.read()

# Step 5: Replace the placeholder with the generated HTML content
new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 6: Write the final HTML to a new file
with open("animals.html", "w", encoding="utf-8") as file:
    file.write(new_html)