while True:
    enemy = hero.findNearestEnemy()
    
    if hero.isReady("cleave"):
        hero.cleave()
        pass
    else:
        hero.attack(enemy)