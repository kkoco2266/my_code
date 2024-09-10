money = 50
print('Amount Due:', money)

while money > 0:
    coin = int(input('Insert Coin: '))
    if coin in [5,10,25]:
        money -= coin
    if money >0:
        print('Amount Due:', money)
else:
    print('Change Owed:', -money)
