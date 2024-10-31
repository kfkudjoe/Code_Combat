
while True:
    enemies = hero.findEnemies()
    nearest = hero.findNearestEnemy()

    if hero.canCast("summon-undead"):
        hero.cast("summon-undead")
        pass
    
    if nearest:
        hero.cast("drain-life", nearest)