while True:
    yak = hero.findNearestEnemy()

    if yak:
        # If the yak is above the hero
        if yak.pos.y > hero.pos.y:
            # Build a "fence" 10m below the yak
            hero.buildXY("fence", hero.pos.x, yak.pos.y - 10)
        # If the yak is below the hero
        else:
            # Build a "fence" 10m above the yak
            hero.buildXY("fence", hero.pos.x, yak.pos.y + 10)
    else:
        x = hero.pos.x + 10
        y = hero.pos.x
        hero.moveXY(x, y)
        pass