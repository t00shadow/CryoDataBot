import csv

def has_entries(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        _ = next(reader, None)                  # read the header row
        return next(reader, None) is not None   # try to read one more row
