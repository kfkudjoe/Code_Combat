# Use modulo to loop over an array.

# Choose the mix and order of units you want to summon by populating this array.
summonTypes = ["archer", "archer", "archer", "soldier"]
defendPos = {'x': 39, 'y': 36}


def collectGold():
    gold = hero.findNearestItem()

    if gold:
        hero.move(gold.pos)

def summonTroops():
    if hero.canCast("summon-undead"):
        hero.cast("summon-undead")
    # Use % to wrap around the summonTypes array based on
    # len(hero.built)
    type = summonTypes[len(hero.built) % len(summonTypes)]

    if hero.gold > hero.costOf(type):
        hero.summon(type) 

def commandTroops():
    friends = hero.findFriends()
    friendIndex = 0

    while friendIndex < len(friends):
        friend = friends[friendIndex]
        friendIndex += 1

        if friend.type == "archer":
            archerEnemy = friend.findNearestEnemy()

            if archerEnemy:
                if archerEnemy.type == "shaman":
                    hero.command(friend, "attack", archerEnemy)
                elif archerEnemy.type == "thrower":
                    hero.command(friend, "attack", archerEnemy)
                elif archerEnemy.type == "ogre":
                    hero.command(friend, "attack", archerEnemy)
                else:
                    hero.command(friend, "attack", archerEnemy)
        elif friend.type == "soldier":
            hero.command(friend, "defend", defendPos)


def main():
    while True:
        collectGold()
        summonTroops()
        commandTroops()


main()