from pathlib import Path
import json

base_path = Path(__file__).parent
input_path = base_path / "listings.json"
output_path = base_path / "available-listings.json"

# Extract data into Python
with open(input_path, "r") as infile:
    contents = json.load(infile)

# Filter out all unavailable job listings.
available = [job for job in contents if job["available"]]

# Write available listings to an output file.
with open(output_path, "w") as outfile:
    json.dump(available, outfile, indent=2)
