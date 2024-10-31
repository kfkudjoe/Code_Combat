wizard = hero.findNearest(hero.findFriends())
yetis = wizard.findEnemies()


for i in range(len(yetis)-1, -1, -1):
    yeti = yetis[i]

    while yeti.health > 0:
        hero.cast("drain-life", yeti)