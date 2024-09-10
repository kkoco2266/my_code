import inflect
p = inflect.engine()

names = []
try:
    while True:
        names.append(input('Name: '))
except EOFError:
    print('Adieu, adieu, to', p.join(names))
