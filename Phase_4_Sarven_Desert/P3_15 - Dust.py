attacks = 0

while attacks < 10:
    enemy = hero.findNearestEnemy()
    
    if enemy:
        hero.cast("drain-life", enemy)
    
    attacks += 1

hero.say("I should retreat!")
hero.moveXY(79, 32)