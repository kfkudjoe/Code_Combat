while True:
    flag = hero.findFlag()

    if flag:
        flagX = flag.pos.x
        flagY = flag.pos.y

        hero.buildXY("fire-trap", flagX, flagY)
        hero.pickUpFlag(flag)
    else:
        item = hero.findNearestItem()

        if item:
            itemX = item.pos.x
            itemY = item.pos.y
            hero.moveXY(itemX, itemY)