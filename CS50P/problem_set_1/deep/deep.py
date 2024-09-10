ans = input('What is the answer to the Great Question of Life, the Universe and Everything? ')

match ans.lower().strip():
    case '42'|'forty-two'|'forty two':
        print('Yes')
    case _:
        print('No')
