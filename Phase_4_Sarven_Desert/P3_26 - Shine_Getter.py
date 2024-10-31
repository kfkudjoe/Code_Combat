while True:
    coins = hero.findItems()
    coinIndex = 0

    while coinIndex < len(coins):
        coin = coins[coinIndex]
        coinIndex += 1

        if coin.value == 3:
            hero.moveXY(coin.pos.x, coin.pos.y)
