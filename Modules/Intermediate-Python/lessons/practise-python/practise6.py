import csv
from pathlib import Path
base_path = Path(__file__).parent
input_path = base_path / "data" / "wages.csv"
output_path = base_path / "data" / "high_wages.csv"

high_wages = []

desired_wage = 40000

with open(input_path, "r") as infile:
    reader =csv.DictReader(infile)
    next(reader)
    for elem in reader:
        print(elem)  # <= Each of these elements are `dict`s, not `list`s!
        if int(elem['annual_wage']) >= desired_wage:
            high_wages.append(elem)
            
with open(output_path, "w") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=high_wages[0].keys())
    writer.writeheader()
    for elem in high_wages:
        writer.writerow(elem)  # Notice that we're passing a dict to writerow.

print(high_wages)