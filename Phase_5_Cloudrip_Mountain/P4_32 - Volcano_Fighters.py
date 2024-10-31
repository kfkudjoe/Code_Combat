# This function finds the left-most unit.
def findMostLeft(units):
    if len(units) == 0:
        return None
    
    mostLeft = units[0]

    for unit in units:
        if unit.pos.x < mostLeft.pos.x:
            mostLeft = unit
    return mostLeft

# This function finds the bottom-most unit.
def findMostBototm(units):
    if len(units) == 0:
        return None

    mostBottom = units[0]

    for unit in units:
        if unit.pos.y < mostBottom.pos.y:
            mostBottom = unit
    return mostBottom


paladins = hero.findByType("paladin")
# Find the top left paladin with findMostLeft function
topLeftPaladin = findMostLeft(paladins)

# Find the bottom right paladin with findMostBottom function
bottomRightPaladin = findMostBottom(paladins)

# Use X coordinate from the top left paladin.
# and the Y coordinate from the bottom right paladin.
xPos = topLeftPaladin.pos.x
yPos = bottomRightPaladin.pos.y

# Move to the {x, y} point from the previous step:
hero.moveXY(xPos, yPos)
# Continue to shield while the volcano is erupting:
while True:
    hero.shield()