def sumHealth(enemies):
    totalHealth = 0
    enemyIndex = 0

    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        enemyIndex += 1
        totalHealth += enemy.health
    return totalHealth


# Use the cannon to defeat the ogres
cannon = hero.findNearest(hero.findFriends())

# The cannon can see through the walls
enemies = cannon.findEnemies()

# Calculate the sum of the ogres' Health
ogreSummaryHealth = sumHealth(enemies)
hero.say("Use" + ogreSummaryHealth + "grams.")