import sys
import csv

people = []

if len(sys.argv) > 3 :
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
# elif sys.argv[1][-4:] != '.csv' :
#     sys.exit('Not a CSV file')

# try:
with open(f'{sys.argv[1]}') as kk:
    before = csv.DictReader(kk)
    for person in before:
           last, first = person['name'].split(',')
           people.append({ 'first' : first.strip() , 'last' : last , 'house' : person['house']})
with open(sys.argv[2], 'w') as yy:
        writer = csv.DictWriter( yy , fieldnames=['first' , 'last' , 'house'])
        writer.writeheader()
        writer.writerows(people)

# except FileNotFoundError:
#     sys.exit(f'Could not read {sys.argv[1]}')
