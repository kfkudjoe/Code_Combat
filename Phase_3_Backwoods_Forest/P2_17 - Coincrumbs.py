while True:
    item = hero.findNearestItem()

    if item:
        itemPosition = item.pos
        itemX = itemPosition.x
        itemY = itemPosition.y

        hero.moveXY(itemX, itemY)
        