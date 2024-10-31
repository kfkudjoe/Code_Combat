while hero.time < 20:
    coin = hero.findNearestItem()
    hero.move(coin.pos)

while hero.pos.x > 16:
    hero.move({'x': 13, 'y': 36})

hero.buildXY("fence", 22, 37)