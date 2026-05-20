import csv
import json

import helper
from pathlib import Path

def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    file_path = Path(__file__).with_name(filename)
    with open(file_path, encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines


def read_airports(filename='airports.dat'):
    # Return a map of code -> name
    airports= {}
    file_path = Path(__file__).with_name(filename)
    with open(file_path, encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            code = line[4]
            name = line[1]
            if code and code != r'\N':
                airports[code] = name

    return airports


def read_routes(filename='routes.dat'):
    # Return a map from source -> list of destinations
    routes = {}
    file_path = Path(__file__).with_name(filename)
    with open(file_path, encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            source = line[2]
            dest = line[4]
            if source and dest and source != r'\N' and dest != r'\N':
                routes.setdefault(source, []).append(dest)
        
    return routes


def find_paths(routes, source, dest, max_segments):
    # Map segment_count -> set of paths (each path is a tuple of airport codes)
    found = {}
    current_paths = [(source,)]  # paths with current segment length

    for segments in range(1, max_segments + 1):
        next_paths = []

        for path in current_paths:
            last_airport = path[-1]
            for neighbor in routes.get(last_airport, []):
                if neighbor in path:
                    continue  # avoid cycles in one path

                new_path = path + (neighbor,)
                next_paths.append(new_path)

                if neighbor == dest:
                    found.setdefault(segments, set()).add(new_path)

        current_paths = next_paths

    return found

def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()

    paths = find_paths(routes, source, dest, max_segments)
    output = {}  # Build a collection of output paths!
    
    # Don't forget to write the output to JSON!
    for segments, segment_paths in paths.items():
        key = str(segments)
        output[key] = [list(rename_path(path, airports)) for path in segment_paths]

    output_path = Path(__file__).with_name('routes.json')
    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(output, outfile, indent=2)

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
