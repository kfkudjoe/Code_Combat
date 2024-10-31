while True:
    enemy = hero.findNearestEnemy()

    if enemy:
        if enemy.type == "burl":
            hero.say("I'm not attacking that Burl!")
        if enemy.type == "munchkin":
            hero.attack(enemy)
        if enemy.type == "thrower":
            hero.attack(enemy)
        if enemy.type == "ogre":
            hero.moveXY(20, 39)