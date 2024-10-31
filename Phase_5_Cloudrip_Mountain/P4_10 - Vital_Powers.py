def pickUpNearestCoin():
    items = hero.findItems()
    nearestCoin = hero.findNearest(items)

    if nearestCoin:
        hero.move(nearestCoin.pos)

def summonSoldier():
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
    pass

def commandSoldiers():
    for soldier in hero.findFriends():
        enemy = soldier.findNearestEnemy()

        if enemy:
            hero.command(soldier, "attack", enemy)


while True:
    if hero.canCast("summon-undead"):
        hero.cast("summon-undead")

    nearestEnemy = hero.findNearestEnemy()

    if (nearestEnemy) and (hero.health < hero.maxHealth / 2):
        hero.cast("drain-life", nearestEnemy)

    pickUpNearestCoin()
    summonSoldier()
    commandSoldiers()