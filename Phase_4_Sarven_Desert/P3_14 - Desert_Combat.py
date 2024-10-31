ordersGiven = 0

while ordersGiven < 5:
    x = hero.pos.x
    y = hero.pos.y

    hero.moveXY(x, y - 10)
    hero.say("Attack!")

    ordersGive +=1


while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        pass
