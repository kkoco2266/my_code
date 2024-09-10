import random

def main():
    n = get_level()
    num_of_ques = 0
    score = 0
    while num_of_ques < 10:
        x = generate_integer(n)
        y = generate_integer(n)
        num_of_ques += 1
        tries = 3
        while tries > 0:
            ans = input(f'{x} + {y} = ').strip()
            if ans == str(x+y):
                tries = 0
                score += 1
            else:
                if tries == 1:
                    tries -= 1
                    print(f'{x} + {y} = {x+y}')
                else:
                    tries -= 1
                    print('EEE')
    print(f'Score: {score}')


def get_level():
    while True:
        try:
            n = int(input('Level: '))
            if not n in [1, 2, 3]:
                raise ValueError
            else:
                return n
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError




if __name__ == "__main__":
    main()
