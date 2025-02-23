#!/bin/bash

# Check if an input file is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

INPUT_FILE="$1"
OUTPUT_FILE="output.txt"

# Check if input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: File '$INPUT_FILE' not found!"
    exit 1
fi

# Process JSON and format output
jq -r '.geometry | map([.lon, .lat]) | map(tostring) | join(",\n")' "$INPUT_FILE" > "$OUTPUT_FILE"

echo "Converted output saved in $OUTPUT_FILE"
