import random
while True:
    try:
        n = int(input('Level:'))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        pass

num = random.randint(1,n)
while True:
    try:
        guess = int(input('Guess: '))
        if guess < 0:
            raise ValueError
        elif guess < num:
            print('Too small!')
            raise ValueError
        elif guess > num:
            print('Too large!')
            raise ValueError
        else:
            print('Just right!')
            break
    except:
        pass
