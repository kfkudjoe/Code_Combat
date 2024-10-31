hero.moveDown()

hero.moveRight()
hero.moveDown()
hero.moveUp()
hero.moveLeft()
hero.moveDown()
hero.moveRight(4)
hero.moveLeft()
hero.moveUp()
hero.moveRight()
hero.moveUp()

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)