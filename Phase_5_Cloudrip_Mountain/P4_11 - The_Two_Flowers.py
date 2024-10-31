def summonSkeletons():
    if hero.canCast("summon-undead"):
        hero.cast("summon-undead")

def summonSoldiers():
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")

def commandSoldiers():
    soldiers = hero.findByType("soldier")
    
    for soldier in soldiers:
        enemy = soldier.findNearestEnemy()
        hero.command(soldier, "attack", enemy)

def pickUpNearestCoin():
    coin = hero.findNearestItem()

    if coin:
        hero.move(coin.pos)


peasant = hero.findByType("peasant")[0]

while True:
    summonSoldiers()
    commandSoldiers()
    pickUpNearestCoin()