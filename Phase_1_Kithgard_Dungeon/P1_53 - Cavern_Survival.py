while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)

    if enemy:
        if distance < 10:
            hero.cast("drain-life", enemy)
        elif distance > 10:
            hero.moveXY(enemy.pos.x, enemy.pos.y)
            pass