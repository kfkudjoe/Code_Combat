import Math

def drawCircle(x, y, size):
    angle = 0
    
    hero.toggleFlowers(False)

    while angle <= Math.PI * 2:
        newX = x + (size * Math.cos(angle))
        newY = y + (size * Math.sin(angle))
        angle += 0.2

        hero.moveXY(newX, newY)
        hero.toggleFlowers(True)


def drawSquare(x, y, size):
    hero.toggleFlowers(False)
    
    cornerOffset = size / 2

    hero.moveXY(x - cornerOffset, y - cornerOffset)
    hero.toggleFlowers(True)

    hero.moveXY(x + cornerOffset, y - cornerOffset)
    hero.moveXY(x + cornerOffset, y + cornerOffset)
    hero.moveXY(x - cornerOffset, y + cornerOffset)
    hero.moveXY(x - cornerOffset, y - cornerOffset)



redX = {'x': 28, 'y': 36}
whiteX = {'x': 44, 'y': 36}

hero.setFlowerColor("purple")
drawCircle(redX.x, redX.y, 10)

hero.setFlowerColo
r("red")
drawSquare(whiteX.x, whiteX.x, 10)