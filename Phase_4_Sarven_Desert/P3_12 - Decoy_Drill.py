decoysBuilt = 0

while True:
    coin = hero.findNearestItem()

    if coin:
        hero.moveXY(coin.pos.x, coin.pos.y)
        pass
    
    if hero.gold >= 25:
        hero.buildXY("decoy", hero.pos.x, hero.pos.y)
        
        decoysBuilt += 1
    
    if decoysBuilt == 4:
        break

hero.say("Done building decoys!")
hero.moveXY(14, 36)
hero.say(decoysBuilt)