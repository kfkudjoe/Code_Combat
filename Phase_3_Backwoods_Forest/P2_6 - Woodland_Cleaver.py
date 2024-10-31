hero.moveXY(23, 23)

def kill(enemy):
    if hero.isReady("cleave"):
        hero.cleave()
        pass
    else:
        hero.attack(enemy)

while True:
    enemy = hero.findNearestEnemy()
    kill(enemy)
    enemy2 = hero.findNearestEnemy()
    kill(enemy)
    enemy3 = hero.findNearestEnemy()
    kill(enemy)
    enemy4 = hero.findNearestEnemy()
    kill(enemy)
    enemy5 = hero.findNearestEnemy()
    kill(enemy)
    enemy6 = hero.findNearestEnemy()
    kill(enemy)