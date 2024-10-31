while True:
    green = hero.findFlag("green")
    black = hero.findFlag("black")
    nearestEnemy = hero.findNearestEnemy()

    if green:
        hero.pickUpFlag(green)
    elif black and hero.isReady("cleave"):
        hero.pickUpFlag(black)
        hero.cleave(nearestEnemy)
    elif nearestEnemy and hero.distanceTo(nearestEnemy) < 10:
        hero.attack(nearestEnemy)
        hero.attack(nearestEnemy)
        pass