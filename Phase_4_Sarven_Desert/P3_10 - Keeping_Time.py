while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()

    if hero.time < 10:
        if enemy.type == "munchkin" or enemy.type == "ogre" or enemy.type == "thrower":
            hero.cast("drain-life", enemy)
        pass
    elif hero.time < 35:
        hero.moveXY(item.pos.x, item.pos.y)
        pass
    else:
        hero.cast("drain-life", enemy)
        pass