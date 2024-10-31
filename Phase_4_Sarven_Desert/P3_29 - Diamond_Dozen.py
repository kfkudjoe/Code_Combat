def findMostHealth(emenies):
    target = None
    targetHealth = 0
    enemyIndex = 0

    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        enemyIndex += 1

        if enemy.health > targetHealth:
            target = enemy
            targetHealth = enemy.health
    return target

def valueOverDistance(item):
    return item.value / hero.distanceTo(item)

# Return the item with the highest valueOverDistance(item)
def findBestItem(items):
    bestItem = None
    bestValue = 0
    itemsIndex = 0

    # Loop over the items array.
    while itemsIndex < len(items):
        item = items[itemsIndex]
        itemsIndex += 1
        itemValueOverDistance = valueOverDistance(item)

        # Find the item with the highest valueOverDistance()
        if itemValueOverDistance > bestValue:
            bestItem = item
            bestValue = itemValueOverDistance
    return bestItem


while True:
    enemies = hero.findEnemies()
    enemy = findMostHealth(enemies)

    if enemy and enemy.heath > 15:
        while enemy.health > 0:
            hero.cast("drain-life", enemy)
    else:
        coins = hero.findItems()
        coin = findBestItem(coins)
        
        if coin:
            hero.moveXY(coin.pos.x, coin.pos.y)