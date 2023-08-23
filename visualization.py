import folium

# Read the polygons from the provided file
with open('formatted_polygons.txt', 'r') as f:
    lines = f.readlines()

# Split the lines into individual polygons using 'A :' as the delimiter
polygons = []
polygon = []
for line in lines:
    if line.startswith('A :'):
        if polygon:
            polygons.append(polygon)
            polygon = []
    if line.strip():
        polygon.append(line.strip())
if polygon:
    polygons.append(polygon)

# Parse the coordinates from the polygons
def parse_coordinate(coord_str):
    lon_str, lat_str = coord_str.split(" / ")
    lon = float(lon_str.split("°")[0]) + float(lon_str.split("°")[1].split("'")[0]) / 60 + float(lon_str.split("'")[1].split("”")[0]) / 3600
    lat = float(lat_str.split("°")[0]) + float(lat_str.split("°")[1].split("'")[0]) / 60 + float(lat_str.split("'")[1].split("”")[0]) / 3600
    if 'W' in lon_str or 'O' in lon_str:
        lon = -lon
    if 'S' in lat_str:
        lat = -lat
    return (lat, lon)

all_coords = []
for polygon in polygons:
    coords = [parse_coordinate(coord.split(":")[1]) for coord in polygon]
    all_coords.extend(coords)

# Compute the center of the map
avg_lat = sum([coord[0] for coord in all_coords]) / len(all_coords)
avg_lon = sum([coord[1] for coord in all_coords]) / len(all_coords)

# Create the folium map
m = folium.Map(location=[avg_lat, avg_lon], zoom_start=10)

# Add each polygon to the map
for polygon in polygons:
    coords = [parse_coordinate(coord.split(":")[1]) for coord in polygon]
    folium.Polygon(locations=coords, color='blue', fill=True, fill_color='blue').add_to(m)

m.save('map.html')
m
