def main():
    word = input('Input: ').strip()
    print('Output:', shorten(word))

def shorten(word):
    ans = ''
    for i in word:
        if i.lower() in ['a','e','i','o','u']:
            continue
        else:
            ans += i
    return ans

if __name__ == "__main__":
    main()
