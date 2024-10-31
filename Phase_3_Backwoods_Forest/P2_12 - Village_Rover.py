def findAndAttackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

while True:
    hero.moveXY(35, 34)
    findAndAttackEnemy()

    hero.moveXY(60, 31)
    findAndAttackEnemy()