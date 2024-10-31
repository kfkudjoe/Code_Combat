hero.moveUp()
hero.moveRight(3)
hero.moveDown(2)

enemy1 = hero.findNearestEnemy()
hero.attack(enemy1)

enemy2 = hero.findNearestEnemy()
hero.attack(enemy2)

hero.moveLeft()
hero.moveDown()