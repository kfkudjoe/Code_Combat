while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        pass
    else:
        hero.moveXY(40, 34)
        pass