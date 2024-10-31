spell = "VENI"
wizard = hero.findNeareast(hero.findFriends())
powerMap = wizard.powerMap


def convert(row, col):
    return {'x': 16 + (12 * col), 'y': 16 + (12 * row)}

for i in range(len(powerMap)):
    # Each row is an array. Iterate through it
    for j in range(len(powerMap[i])):
        pointValue = powerMap[i][j]

        if pointValue > 0:
            coords = convert(i, j)

            hero.moveXY(coords.x, coords.y)
            hero.say(spell)
            
            enemy = hero.findNearestEnemy()
            if enemy:
                while enemy.health > 0:
                    hero.cast("drain-life", enemy)
            
            item = hero.findNearestItem()
            if item and item.type == "potion":
                hero.moveXY(item.pos.x, item.pos.y)