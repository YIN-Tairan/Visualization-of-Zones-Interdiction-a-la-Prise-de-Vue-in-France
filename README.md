
# Visualization of Zones Interdites à la Prise de Vue Aérienne (Aerial Imaging Prohibited Zones) in France

This repository provides a visualization of areas in France where aerial imaging is prohibited, officially known as "Zones Interdites à la Prise de Vue Aérienne". As the use of drones for aerial photography and videography becomes more widespread, understanding where imaging is restricted is vital for legal and privacy reasons.

## Data Source

The coordinate data for the aerial imaging prohibited zones, "Zones Interdites à la Prise de Vue Aérienne", is sourced from the official French government website: [Légifrance](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000041459817). The specific data was extracted using the browser's developer tools (F12) and copying the outer HTML of the embedded table containing the zone details.

## Data Processing

1. **Extraction**: The raw HTML data was saved to a file named `web.txt`.
2. **Parsing**: From this raw data, relevant coordinates describing the polygons of aerial imaging prohibited zones were extracted and formatted.
3. **Conversion**: The coordinates were in the Degrees, Minutes, Seconds (DMS) format. They were converted to the Decimal Degrees format, which is more suited for visualization tools.


## Visualization

With the cleaned and converted data, we used Python libraries to visualize these "Zones Interdites à la Prise de Vue Aérienne" on a map. This visualization assists individuals and entities in identifying where aerial imaging is prohibited, ensuring they adhere to local regulations and respect privacy constraints.

## Usage through Google Colab
1. Create a new colab project and copy-paste the *colab.py* 
2. Import the file *formatted_polygons.txt* into the session's storage space
3. Run the code.

## Use through local clone
1. Clone this repository.
2. Install necessary Python libraries.
3. Run the script *visualization.py* to generate a map highlighting the "Zones Interdites à la Prise de Vue Aérienne".
4. Use this map as a reference before undertaking aerial photography or videography in France.

## Attention
1. The visualization is not perfect and contains artifacts caused by some incorrect coordinate seperation. It gives however a rough idea of the extent of these restricted areas.
2. The results of visualization are only indicative and not verified. The creation of this project is because I couldn't find an official visulisation, and it is impossible to see where the restricted areas are with only a list of coordinates. 
3. The list was fixed on 2020 and the data may not be up-to-date. Should you find a newer list, you can repeat the approach with the codes that I provided here.

## Credits

All coding, data processing, and visualization logic were provided by OpenAI's Assistant. Special thanks to the Assistant for making this visualization possible.
