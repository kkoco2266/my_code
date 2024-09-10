import sys

num_of_rows = 0

if len(sys.argv) > 2 :
    sys.exit('Too many command-line arguments')
elif len(sys.argv) == 1:
    sys.exit('Too few command-line arguments')
elif sys.argv[1][-3:] != '.py' :
    sys.exit('Not a Python file')

try:
    with open(f'{sys.argv[1]}') as kk:
        for row in kk:
            try:
                elem_1 = row.lstrip()[0]
            except IndexError :
                continue
            if elem_1 == '#' :
                continue
            else:
                num_of_rows += 1
except FileNotFoundError:
    sys.exit('File does not exist')

print(num_of_rows)
