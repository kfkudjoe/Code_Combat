def drawConcentricCircles (x, y, numCircles, spacing):
    hero.toggleFlowers(False)

    for i in range(numCircles):
        size = (i + 1) * spacing
        drawCircle(x, y, size)

def drawCircle(x, y, size):
    angle = 0
    hero.toggleFlowers(False)

    while angle <= Math.PI * 2:
        newX = None
        newY = None

        angle += 0.2

        hero.moveX(newX, newY)
        hero.toggleFlowers(True)


redX = {'x': 88, 'y': 70}

hero.setFlowerColor("purple")
drawConcentricCircles(redX.x, redX.y, 5, 10)