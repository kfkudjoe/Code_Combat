while True:
    farthest = None
    maxDistance = 0
    enemyIndex = 0
    enemies = hero.findEnemies()

    while enemyIndex < len(enemies):
        target = enemies[enemyIndex]
        enemyIndex += 1
        distance = hero.distanceTo(target)

        if distance > maxDistance:
            maxDistance = distance
            farthest = target

    if farthest:
        hero.say(farthest.type)
        
        if hero.canCast("chain-lightning"):
            hero.cast("chain-lightning", farthest)
        elif hero.canCast("poison-cloud"):
            hero.cast("poison-cloud", farthest)
        else:
            hero.cast("drain-life", farthest)
        pass