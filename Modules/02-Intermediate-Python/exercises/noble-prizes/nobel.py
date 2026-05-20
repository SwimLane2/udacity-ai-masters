import json

import helper

from pathlib import Path


def load_nobel_prizes(filename='prize.json'):
    file_path = Path(__file__).with_name(filename)
    with open(file_path, "r") as infile:
        return json.load(infile)


def main(year, category):
    data = load_nobel_prizes()
    # Add more here!
    prizes = data["prizes"]
    if year is not None:
        prizes = [prize for prize in prizes if prize["year"] == year]

        
    if category is not None:
        prizes = [prize for prize in prizes if prize["category"] == category.lower()]

    for prize in prizes:
        print(f"{prize['year']} - {prize['category']}")



if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)

