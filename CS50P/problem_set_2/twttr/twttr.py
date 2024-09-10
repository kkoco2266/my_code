word = input('Input: ').strip()
ans = ''
for i in word:
    if i.lower() in ['a','e','i','o','u']:
        continue
    else:
        ans += i
print('Output:', ans)

