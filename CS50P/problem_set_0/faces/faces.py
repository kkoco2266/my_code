def main():
    emoticon = input()
    emoji = convert(emoticon)
    print(emoji)

def convert(fr):
    to = fr.replace(':)', '🙂').replace(':(', '🙁')
    return to

main()
