while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)

    if hero.isReady("cleave"):
        hero.cleave()
        pass
    elif distance < 5:
        hero.attack(enemy)
    else:
        hero.attack("Chest")
        pass