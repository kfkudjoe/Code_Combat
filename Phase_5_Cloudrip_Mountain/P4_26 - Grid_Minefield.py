# Use nested loops to build the grid minefield.

# First iterate x coordinates from 12 to 60 with a step size of 8.
for x in range(12, 60, 8):

    # For each x, iterate y coordinates from 12 to 68 with a step size of 8/
    for y in range(12, 68, 8):

        # For each point build "fire-trap" there.
        point = {'x': x, 'y': y}
        hero.buildXY("fire-trap", point.x, point.y)

    # After each column, move right to avoid traps
    hero.moveXY(hero.pos.x + 8, hero.pos.y)

# Move to the nearest mine when the ogres are close.
while True:
    enemy = hero.findNearestEnemy()

    if enemy:
        distance = hero.distanceTo(enemy)

        if distance <= 20:
            hero.moveXY(point.x, point.y)