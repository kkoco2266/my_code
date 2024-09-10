def main():
    while True:
        try:
            fraction = input('Fraction: ').strip()
            percentage = convert(fraction)
            break
        except (ZeroDivisionError, ValueError):
            pass
    print(gauge(percentage))

def convert(fraction):
    x, y = fraction.replace('/', ' ').split()
    x = int(x)
    y = int(y)
    k = round(x/y*100)
    if x > y:
        raise ValueError
    return k

def gauge(percentage):
    if 0 <= percentage <= 1:
          return 'E'
    elif 99<= percentage <=100:
          return 'F'
    else:
          return str(percentage) + '%'


if __name__ == "__main__":
    main()
