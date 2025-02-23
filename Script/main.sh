#!/bin/bash

# Check if input file is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <inputfile.json>"
    exit 1
fi

# Input file from command-line argument
INPUT_FILE="$1"
OUTPUT_FILE="output.geojson"

# Convert Overpass JSON to GeoJSON
jq '{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "IND",
      "properties": { "name": "India" },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            (.elements[] | select(.type == "relation") | .members[] | select(.type == "way") | .geometry[] | [ .lon, .lat ])
          ]
        ]
      }
    }
  ]
}' "$INPUT_FILE" > "$OUTPUT_FILE"

echo "Converted to GeoJSON: $OUTPUT_FILE"

#(.elements[] | select(.type == "relation") | .members[] | select(.type == "way") | .geometry[] | [ .lon, .lat ])
