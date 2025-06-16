import json

# Step 1: Load the animal data from the JSON file
with open("animals_data.json", "r") as file:
    animals = json.load(file)

# Step 2: Create an empty string to collect HTML content
output = ""

# Step 3: Loop through each animal in the data list
for animal in animals:
    # Get the name of the animal (if it exists)
    name = animal.get("name")

    # Get the diet from the characteristics (if it exists)
    diet = animal.get("characteristics", {}).get("diet")

    # Get the first location from the list (if it exists)
    locations = animal.get("locations")
    location = locations[0] if locations else None

    # Get the type from the characteristics (if it exists)
    animal_type = animal.get("characteristics", {}).get("type")

    # Step 4: Add information to the HTML string (only if data exists)
    output += "<p>\n"
    if name:
        output += f"<strong>Name:</strong> {name}<br>\n"
    if diet:
        output += f"<strong>Diet:</strong> {diet}<br>\n"
    if location:
        output += f"<strong>Location:</strong> {location}<br>\n"
    if animal_type:
        output += f"<strong>Type:</strong> {animal_type}<br>\n"
    output += "</p>\n\n"

# Step 5: Read the HTML template from file
with open("animals_template.html", "r") as file:
    template = file.read()

# Step 6: Replace the placeholder with the actual HTML output
new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 7: Save the final HTML to a new file
with open("animals.html", "w") as file:
    file.write(new_html)