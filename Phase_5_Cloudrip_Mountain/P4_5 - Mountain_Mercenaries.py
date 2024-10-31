while True:
    coins = hero.findItems()
    coinIndex = 0
    while coinIndex < len(coins):
        coin = coins[coinIndex]
        coin += 1
        hero.move(coin.pos)

if hero.gold > hero.costOf("soldier"):
    hero.summon("soldier")

enemy = hero.findNearest(hero.findEnemies())

if enemy:
    soldiers = hero.findFriends()
    soldierIndex = 0

    while soldierIndex < len(soldiers):
        soldier = soldiers[soldierIndex]
        soldierIndex += 1

        hero.command(soldier, "attack", enemy)