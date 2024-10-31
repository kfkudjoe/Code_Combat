while True:
    enemy = hero.findNearestEnemy()

    if enemy:
        hero.cast("drain-life", enemy)
    else:
        x = hero.pos.x + 2
        y = hero.pos.y + 2
        hero.moveXY(x, y)
    pass