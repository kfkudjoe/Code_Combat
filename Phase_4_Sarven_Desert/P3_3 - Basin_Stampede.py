while True:
    enemy = hero.findNearestEnemy()
    xPos = hero.pos.x + 5
    yPos = 17

    if enemy:
        if enemy.pos.y > hero.pos.y:
            yPos -= 3
            pass
        elif enemy.pos.y < hero.pos.y:
            yPos += 3
            pass
    
    hero.moveXY(xPos, yPos)