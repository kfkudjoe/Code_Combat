while True:
    x = hero.pos.x
    y = hero.pox.y

    yak = hero.findNearestEnemy()

    if hero.distanceTo(yak) < 10:
        x = x + 10
        hero.moveXY(x, y)