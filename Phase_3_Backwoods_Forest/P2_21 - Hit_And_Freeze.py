def inAttackRange(enemy):
    distance = hero.distanceTo(enemy)

    if distance <= 3:
        return True
    else:
        return False

while True:
    nearestEnemy = hero.findNearestEnemy()
    canAttack = inAttackRange(nearestEnemy)

    if canAttack:
        hero.attack(nearestEnemy)
    pass