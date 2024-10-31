defeatedOgres = 0

# This loop is executed when defeatedOgres is less than 6.
while defeatedOgres < 6:
    enemy = hero.findNearestEnemy()
    
    if enemy:
        hero.cast("drain-life", enemy)
    else:
        hero.say("Ogres!")

# Move to the right side of the map.
hero.moveXY(49, 36)

# This loop is executed while you have less than 30 gold.
while hero.gold < 30:
    # Find and collect coins.
    coin = hero.findNearestItem()
    hero.moveXY(coin.pos.x, coin.pos.y)

# Move to the exit.
hero.moveXY(76, 32)