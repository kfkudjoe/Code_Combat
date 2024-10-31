def dealEnemy(enemy):
    if enemy.type == "munchkin":
        hero.attack(enemy)
    elif enemy.type == "brawler":
        hero.say(enemy + ", You shall not pass!")
    pass

while True:
    enemy = hero.findNearestEnemy()

    if enemy:
        dealEnemy(enemy)
    else:
        hero.moveXY(30, 34)