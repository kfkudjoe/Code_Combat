# Modulo operator can be used to wrap around to the beginning of an array
# when an index might be greater than the length

defendPoints = [
    {'x': 35, 'y': 65},
    {'x': 61, 'y': 63},
    {'x': 32, 'y': 26},
    {'x': 64, 'y': 26},
]
summonTypes = [
    "soldier", "soldier", "soldier", "soldier", \
    "archer", "archer", "archer", "archer", 
]


# self.built is an array of all troops ever built.
# The operation "len(self.built) % len(summonTypes)"
# is used to wrap around the summonTypes array
def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]

    if hero.gold >= hero.costOf(type):
        hero.summon(type)

def commandTroops():
    friends = hero.findFriends()

    for i in range(len(friends)):
        friend = friends[i]
        # Use % to wrap around defendPoints based on friendIndex.
        defendPoint = defendPoints[i % len(defendPoints)]
        
        # Command your minion to defend the defendPoint
        if friend.health < friend.maxHealth / 2:
            hero.command(friend, "defend", hero)
        else:
            hero.command(friend, "defend", defendPoint)

def main():
    summonTroops()
    commandTroops()

    if hero.canCast("summon-undead"):
        hero.cast("summon-undead")

    enemy = hero.findNearestEnemy()

    if enemy:
        hero.cast("drain-life", enemy)


main()
