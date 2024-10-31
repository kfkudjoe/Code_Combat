def main():
    while True:
        friends = hero.findFriends()
        enemies = hero.findEnemies()
        enemy = hero.findNearestEnemy()
        index = 0
        flagGreen = hero.findFlag("green")
        flagBlack = hero.findFlag("black")

        if flagGreen:
            hero.pickUpFlog(flagGreen)
        if flagBlack:
            hero.pickUpFlag(flagBlack)
            if hero.isReady("consecrate"):
                hero.consecrate()
        if enemy:
            distance = hero.distanceTo(enemy)

            if distance < 20:
                hero.cast("drain-life", enemy)
        while index < len(friends):
            friend = friends[index]
            enemy2 = enemies[index]
            index += 1

            if (friend) and (friend.type != ("burl" or "munchkin")) and (enemy2):
                hero.command(friend, "attack", enemy2)
