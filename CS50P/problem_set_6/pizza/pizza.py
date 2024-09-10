import sys
import csv
from tabulate import tabulate

items = []

if len(sys.argv) > 2 :
    sys.exit('Too many command-line arguments')
elif len(sys.argv) == 1:
    sys.exit('Too few command-line arguments')
elif sys.argv[1][-4:] != '.csv' :
    sys.exit('Not a CSV file')

try:
    with open(f'{sys.argv[1]}') as kk:
       menu = csv.DictReader(kk)
       for item in menu:
           items.append(item)
    print(tabulate(items, headers = 'keys', tablefmt = 'grid'))

except FileNotFoundError:
    sys.exit('File does not exist')
