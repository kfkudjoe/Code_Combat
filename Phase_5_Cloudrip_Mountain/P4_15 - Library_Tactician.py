def findStrongestTarget():
    mostHealth = 0
    bestTarget = None
    enemies = hero.findEnemies()

    for enemy in enemies:
        if enemy.health > mostHealth:
            mostHealth = enemy.health
            bestTarget = enemy
    
    if bestTarget and bestTarget.health > 15:
        return bestTarget
    else:
        return None

def commandArcher(archer):
    nearest = archer.findNearestEnemy()

    if archerTarget:
        hero.command(archer, "attack", archerTarget)
    elif nearest:
        hero.command(archer, "attack", nearest)

def commandSoldier(soldier, soldierIndex, numSoldiers):
    angle = Math.PI * 2 * soldierIndex / numSoldiers
    defendPos = {'x': 41, 'y': 40}
    defendPos.x += 10 * Math.cos(angle)
    defendPos.y += 10 * Math.sin(angle)

    hero.command(soldier, "defend", defendPos)

def main():
    while True:
        friends = hero.findFriends()
        soldiers = hero.findByType("soldier")
        archers = hero.findByType("archer")

    # If archerTarget doesn't exist, find a new one
    if not archerTarget or archerTarget.health < 0:
        archerTarget = findStrongestTarget()
    
    for i in range(len(soldiers)):
        soldier = soldiers[i]

        if soldier.health < soldier.maxHealth / 3:
            hero.command(soldier, "move", {'x': 41, 'y': 40})
        else:
            commandSoldier(soldier, i, len(soldiers));
    
    # use commandArcher() to command your archers
    for archer in archers:
        commandArcher(archer)


archerTarget = None

main()