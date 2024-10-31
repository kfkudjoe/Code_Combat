while True:
    coins = hero.findItems()
    coinIndex = 0
    nearest = None
    nearestDistance = 9999

    while coinIndex < len(coins):
        coin = coins[coinIndex]
        coinIndex += 1
        distance = hero.distanceTo(coin)

        if distance < nearestDistance:
            nearest = coin
            nearestDistance = distance

    if nearest:
        hero.moveXY(nearest.pos.x, nearest.pos.y)