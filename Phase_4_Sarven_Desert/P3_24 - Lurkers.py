enemies = hero.findEnemies()
enemyIndex = 0

while enemyIndex < len(enemies):
    enemy = enemies[enemyIndex]
    enemyIndex += 1

    if enemy.type == "shaman":
        while enemy.health > 0:
            hero.cast("drain-life", enemy)