while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()

    if flag:
        hero.moveXY(flag.pos.x, flag.pos.y)
    elif enemy:
        hero.attack(enemy)
    elif item:
        if item.type == "coin":
            hero.moveXY(item.pos.x, item.pos.y)
