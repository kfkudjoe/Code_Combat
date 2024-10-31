
def maybeBuildTrap(x, y):
    hero.moveXY(x, y)

    enemy = hero.findNearestEnemy()

    if enemy:
        hero.buildXY("fire-trap", x, y)


while True:
    maybeBuildTrap(43, 50)
    maybeBuildTrap(24, 34)
    maybeBuildTrap(43, 20)