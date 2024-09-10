greeting = input('Greeting: ')
gre = greeting.lower().strip()

if 'hello' in gre:
    print('$0')
elif gre[0] == 'h':
    print('$20')
else:
    print('$100')
