def summonTroops():
    if hero.gold > hero.costOf("griffin-rider"):
        hero.summon("griffin-rider")

# Find the paladin with the lowest health
def lowestHealthPaladin():
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()

    for friend in friiends:
        if friend.type != "paladin":
            continue
        if (friend.health < lowestHealth) and (friend.health < friend.maxHealth):
            lowestHealth = friend.health
            lowestFriend = friend

def commandPaladin(paladin):
    # Heal the paladin with the lowest health using lowestHealthPaladin()
    # You can use paladin.canCast("heal") and command(paladin, "cast", "heal", target)
    # Paladins can also shield: command(paladin, "shield")
    # Paladins can also attack: command(paladin, "attack", enemy)
    lowestFriend = lowestHealthPaladin()

    if paladin.canCast("heal") and lowestFriend:
        hero.command(paladin, cast, "heal", lowestFriend)
    elif paladin.health < 200:
        hero.command(paladin, "shield")
    else:
        enemy = paladin.findNearestEnemy()
        
        if enemy:
            hero.command(paladin, "attack", enemy)
    pass

def commandPeasant(friend):
    item = friend.findNearestItem()

    if item:
        hero.command(friend, "move", item.pos)
    pass

def commandGriffin(friend):
    target = hero.findNearest("warlock", hero.findEnemies())

    if not target:
        target = friend.findNearestEnemy()
    if target:
        hero.command(friend, "attack", target)
    pass

def commandFriends():
    # Commmand your allies.
    friends = hero.findFriends()

    for friend in friends:
        if friend.type == "peasant":
            commandPeasant(friend)
            pass
        elif friend.type == "griffin-rider":
            commandGriffin(friend)
            pass
        elif friend.type == "paladin":
            commandPaladin(friend)
            pass

def main():
    commandFriends()
    summonTroops()


main()