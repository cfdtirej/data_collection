import csv
from pathlib import Path

csv_dir = Path(__file__).parent / 'demand_csv'

csv_list = csv_dir.glob('**/*.csv')

print(list(csv_list))