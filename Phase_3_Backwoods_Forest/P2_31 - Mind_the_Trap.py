while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()

    if flag:
        hero.moveXY(flag.pos.x, flag.pos.y)
        hero.say("I should pick up the flag.")
    elif enemy:
        distance = hero.distanceTo(enemy)
        if distance < 30:
            hero.attack(enemy)
