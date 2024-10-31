while True:
    evilstone = hero.findNearestItem()

    if evilstone:
        pos = evilstone.pos
        if pos.x == 34:
            hero.moveXY(46, 23)
            pass
        else:
            if pos.x == 46:
                hero.moveXY(34, 23)
            pass
    else:
        if not evilstone:
            hero.moveXY(40, 23)
        pass