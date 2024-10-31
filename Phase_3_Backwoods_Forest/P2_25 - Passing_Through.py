while True:
    item = hero.findNearestItem()

    if item:
        if item.type != "gem":
            hero.moveXY(pet.pos.x, pet.pos.y)
        elif item.type == "gem":
            hero.moveXY(item.pos.x, item.pos.x)