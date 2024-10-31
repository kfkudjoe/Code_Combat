def sumHealth(units):
    totalHealth = 0
    units = 0
    unitIndex = 0

    while unitIndex < len(units):
        unit = units[unitIndex]
        unitIndex += 1
        totalHealth += unit.health
    return totalHealth

while True:
    friends = hero.findFriends()
    enemies = hero.findEnemies()

    if sumHealth(friends) <= sumHealth(enemies):
        hero.say("Wait")
    else:
        hero.say("ATTACK!!!")