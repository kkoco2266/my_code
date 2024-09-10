groc ={}
while True:
    try:
        itm = input().upper()
        if not itm in sorted(groc):
            groc[itm] = 1
        else:
            groc[itm] += 1
    except EOFError:
        break
for i in sorted(groc):
    print(groc[i], i)
