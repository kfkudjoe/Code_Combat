while True:
    enemy = hero.findNearestEnemy()
    currentHealth = hero.health
    healingThreshold = hero.maxHealth / 2

    if currentHealth < healingThreshold:
        hero.moveXY(65, 48)
        hero.say("heal me")
    else:
        if enemy:
            hero.cast("drain-life", enemy)
            hero.cast("drain-life", enemy)
            hero.cast("drain-life", enemy)