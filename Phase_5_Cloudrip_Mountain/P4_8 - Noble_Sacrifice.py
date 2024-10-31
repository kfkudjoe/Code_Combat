# Collect 80 Gold.
while hero.gold < 80:
    coin = hero.findNearestItem()
    hero.move(coin.pos)

# Build 4 soldiers to use as bait
while hero.gold > hero.costOf("soldier"):
    hero.summon("soldier")
    pass

# Send soldiers into position
points = [
    {'x': 13, 'y': 73},
    {'x': 51, 'y': 73},
    {'x': 51, 'y': 53},
    {'x': 90, 'y': 52},
]
pointIndex = 0

# Match the friends to the points and command them to move
while pointIndex < len(points):
    enemies = hero.findEnemies()
    friends = hero.findFriends()
    
    enemy = enemies[pointIndex]
    friend = friends[pointIndex]
    point = points[pointIndex]
    pointIndex += 1

    if friend:
        if enemy:
            hero.command(friend, 'attack', enemy)
        else:
            hero.command(friend, 'move', point)

    enemies = hero.findEnemies()
    friends = hero.findFriends()