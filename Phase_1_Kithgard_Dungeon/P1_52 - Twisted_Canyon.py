def kill_enemy():
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)

hero.moveUp(3)
kill_enemy()
hero.moveRight(2)
hero.moveLeft(2)

hero.moveDown(4)
hero.moveRight(2)
hero.moveUp()

while True:
    hero.moveLeft()
    kill_enemy()
    hero.moveUp(2)
    hero.moveDown(2)
    hero.moveRight(2)
    hero.moveUp()
    hero.moveRight()
    hero.moveUp()