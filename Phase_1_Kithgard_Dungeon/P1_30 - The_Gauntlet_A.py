while True:
    hero.moveLeft()
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.attack(enemy)