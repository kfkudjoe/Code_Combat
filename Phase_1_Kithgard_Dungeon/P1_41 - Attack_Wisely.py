hero.moveUp(2)

hero.attack("Door A")

hero.moveUp(2)
enemy = hero.findNearestEnemy()

if enemy:
    hero.attack(enemy)
    hero.attack(enemy)

hero.moveDown(3)
hero.moveRight(2)
hero.moveUp()
hero.attack("Door B")
hero.moveUp(2)

enemy = hero.findNearestEnemy()
if enemy:
    hero.attack(enemy)

hero.moveDown(2)
hero.moveRight(2)
hero.attack("Door C")
hero.moveUp(2)
enemy = hero.findNearestEnemy()

if enemy:
    hero.attack(enemy)
    hero.attack(enemy)

hero.moveDown(2)
hero.moveRight(3)

for i in range(2):
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

hero.moveUp(3)
hero.moveLeft()
hero.moveDown(4)
hero.moveLeft(2)
hero.moveDown()
hero.moveLeft(2)