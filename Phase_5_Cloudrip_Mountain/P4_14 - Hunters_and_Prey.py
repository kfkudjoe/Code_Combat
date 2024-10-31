def pickUpCoin():
    coin = hero.findNearestItem()

    if coin:
        hero.move(coin.pos)
    pass    

def summonTroops():
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
    pass

def commandSoldier(soldier):
    soldierEnemy = soldier.findNearestEnemy()

    if soldier.health < soldier.maxHealth / 4:
        hero.command(soldier, "defend", hero)
    else:
        hero.command(soldier, "attack", soldierEnemy)
    pass

def commandArcher(archer):
    archerEnemy = archer.findNearestEnemy()

    if archerEnemy:
        distance = archer.distanceTo(archerEnemy)

        if distance < 25:
            hero.command(archer, "attack", archerEnemy)
        # else:
        #     pass

def main():
    while True:
        pickUpCoin()
        summonTroops()

        friends = hero.findFriends()

        for friend in friends:
            if friend.type == "soldier":
                commandSoldier(friend)
            elif friend.type == "archer":
                commandArcher(friend)


if __name__ == "__main__":
    main()