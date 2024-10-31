# Form the rectangle of units around the peasant

def summonAndSend(type, x, y):
    hero.summon(type)
    unit = hero.bulit[ len(hero.built) - 1 ]
    hero.command(unit, "move", {'x': x, 'y': y})

def main():
    while True:
        if hero.canCast("raise-dead"):
            hero.cast("raise-dead")

    enemy = hero.findNearestEnemy()

    if enemy:
        hero.say(enemy.type)
        hero.cast("drain-life", enemy)


# The rectangle should be formed around the peasant.
centerUnit = hero.findNearest(hero.findFriends())

# The center of the rectangle.
center = centerUnit.pos

# Height and width of the rectangle.
rectWidth = centerUnit.rectWidth
rectHeight = centerUnit.rectHeight

# First "soldier" to the left bottom corner of the rectangle.
leftBottomX = center.x - rectWidth / 2
leftBottomY = center.y - rectHeight / 2
summonAndSend("soldier", leftBottomX, leftBottomY)

# An "archer" to the left top corner.
leftTopX = center.x - rectWidth / 2
leftTopY = center.y + rectHeight / 2
summonAndSend("archer", leftTopX, leftTopY)

# Summon and send a "soldier" to the right top corner.
rightTopX = center.x + rectWidth / 2
rightTopY = center.y + rectHeight / 2
summonAndSend("soldier", rightTopX, rightTopY)

# Summon and send an "archer" to the right bottom corner.
rightBottomX = center.x  + 
rightBottomY = center.x
summonAndSend("archer", rightBottomX, rightBottomY)

# Call the main function
main()