items = hero.findItems()

gem0 = items[0]

hero.say("Bruno" + gem0)
hero.say("Matilda" + items[1])

gem3 = items[2]

hero.moveXY(gem3.pos.x, gem3.pos.y)