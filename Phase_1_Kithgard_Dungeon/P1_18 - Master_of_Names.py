# Assign the result of hero.findNearestEnemy() to the variable enemy1
enemy1 = hero.findNearestEnemy()

# enemy1 now refers to the nearest enemy. Use the variable to attack?
hero.attack(enemy1)
hero.attack(enemy1)

# Now that enemy1 is defeated, calling hero.findNearestEnemy() again will result in finding the the new nearest enemy
enemy2 = hero.findNearestEnemy()

hero.attack(enemy2)
hero.attack(enemy2)

# Assign the result of hero.findNearestEnemy() to the variable enemy3
enemy3 = hero.findNearestEnemy()

hero.attack(enemy3)
hero.attack(enemy3)