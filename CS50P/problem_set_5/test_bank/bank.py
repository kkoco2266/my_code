def main():
    greeting = input('Greeting: ').strip()
    print(f'${value(greeting)}')

def value(greeting):
    gre = greeting.lower()
    if 'hello' in gre:
        return 0
    elif gre[0] == 'h':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
