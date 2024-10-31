while True:
    enemy = hero.findNearestEnemy()

    if enemy:
        # If enemy is to the left of the hero
        if enemy.pos.x < hero.pos.x:
            # Build a fire trap on the left X
            hero.buildXY("fire-trap", 25, 34)
            pass
        # If the enemy is to the right of the hero
        elif enemy.pos.x > hero.pos.x:
            # Build a fire trap on the right x
            hero.buildXY("fire-trap", 55, 34)
            pass
        # If the enemy is below the hero
        elif enemy.pos.y < hero.pos.y:
            # Build a fire trap on the bottom X
            hero.buildXY("fire-trap", 40, 19)
            pass
        # If the enemy is above the hero
        elif enemy.pos.y > hero.pos.y:
            # Build a fire trap on the top X
            hero.buildXY("fire-trap", 40, 49)
            pass
    
    hero.moveXY(40, 34)