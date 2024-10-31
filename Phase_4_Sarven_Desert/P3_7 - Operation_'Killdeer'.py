def shouldRun():
    if hero.health < hero.maxHealth / 2:
        return True
    else:
        return False

while True:
    enemy = hero.findNearestEnemy()

    if shouldRun():
        hero.moveXY(75,37)
    elif hero.canCast("chain-lighting"):
        hero.cast("chain-lightning", enemy)
    else:
        hero.cast("drain-life", enemy)
        hero.cast("drain-life", enemy)
        hero.cast("drain-life", enemy)