def chooseTarget(friend):
    """
    The chooseTarget function takes a friend argument.
    The chooseTarget function returns a target to attack, depending on the type of friend.
    Soldiers attack witches, archers attack the nearest enemy.
    """
    if friend.type == "soldier":
        witches = friend.findByType("witch")

        if len(witches) > 0
            return witches[0]
    
    elif friend.type == "archer":
        enemies = friend.findEnemies()

        for enemy in enemies:
            if enemy.type == "thrower":
                return enemy
            elif enemy.type == "ogre":
                return enemy
            else:
                return friend.findNearestEnemy()
    return None


def main():
    while True:
        friends = hero.findFriends()
        enemies = hero.findEnemies()

        if hero.canCast("summon-yeti"):
            hero.cast("summon-yeti")

        for friend in friends:
            target = chooseTarget(friend)

            if target:
                hero.command(friend, "attack", target)


main()