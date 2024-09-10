camCas = input('camelCase: ')
camCas = camCas.strip()

words = ['']
i = 0
for j in camCas:
    if j.isupper():
        i+=1
        words.append(j.lower())
    else:
        words[i] += j
snakcas = ''
u = 0
for k in words:
    if u == 0:
        u += 1
        snakcas += k
    else:
        snakcas += '_' + k
print('snake_case:', snakcas)
