def main():
        print(get_per())

def get_per():
    while True:
        try:
            x, y = input('Fraction: ').replace('/', ' ').split()
            x = int(x)
            y = int(y)
            if x > y:
                raise ValueError
            perc = round(x/y*100)
            return ans(perc)
        except (ZeroDivisionError, ValueError):
            pass

def ans(p):
     if 0 <= p <= 1:
          return 'E'
     elif 99<= p <=100:
          return 'F'
     else:
          return str(p) + '%'

main()
