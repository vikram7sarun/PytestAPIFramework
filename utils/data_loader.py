# utils/data_loader.py
import json
import csv

def load_json_data(file_path):
    with open(file_path) as f:
        return json.load(f)

def load_csv_data(file_path):
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
