import re
from itertools import groupby

# Function to normalize the DMS strings to a consistent format
def normalize_dms(dms_str):
    return dms_str.replace("”", "\"").replace("’", "'").replace("°", "d")

# Function to split the raw coordinate data into individual coordinates
def split_coordinates(raw_data):
    pattern = r'[A-Z] : [\d\s°\'”d]+ E / [\d\s°\'”d]+ N|[A-Z] : [\d\s°\'”d]+ W / [\d\s°\'”d]+ N|[A-Z] : [\d\s°\'”d]+ O / [\d\s°\'”d]+ N|[A-Z] : [\d\s°\'”d]+ E / [\d\s°\'”d]+ S|[A-Z] : [\d\s°\'”d]+ W / [\d\s°\'”d]+ S|[A-Z] : [\d\s°\'”d]+ O / [\d\s°\'”d]+ S'
    return re.findall(pattern, raw_data)

# Read the raw data from the uploaded file
with open('/path/to/web.txt', 'r') as f:
    raw_data = f.read()

# Normalize and split the raw data into individual coordinates
normalized_coordinates = [normalize_dms(coord) for coord in split_coordinates(raw_data)]

# Split the normalized coordinates into individual polygons
normalized_polygons = [list(g) for k, g in groupby(normalized_coordinates, lambda x: x == "") if not k]

# Extract and format the coordinates to the specified format
formatted_polygons = []

for raw_polygon in normalized_polygons:
    formatted_coords = []
    for coord in raw_polygon:
        lon, lat = coord.split(" : ")[1].split(" / ")
        formatted_coord = "{} : {} / {}".format(coord.split(' : ')[0], lon.replace('d', '°').replace('"', '”'), lat.replace('d', '°').replace('"', '”'))
        formatted_coords.append(formatted_coord)
    formatted_polygons.append(formatted_coords)

# Write the formatted polygons to a text file
with open('/path/to/formatted_polygons.txt', 'w') as f:
    for polygon in formatted_polygons:
        for coord in polygon:
            f.write(coord)
            f.write("\n")
        f.write("\n")
