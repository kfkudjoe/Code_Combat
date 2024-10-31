"""
We need to build guard towers around the village.
Each peasant can build one tower.
We have to direct them to where to build.
The towers are automatic and will attack ALL units outside the town.
"""

# First move along the north border (y = 60) from x = 40 to x = 80, with a step size of 20.
for x in range(20, 81, 20):
    hero.moveXY(x, 60)
    hero.say("Here")

# Next move along the east border (x = 80) from y = 40 to y = 20 with step size of -20.
for y in range(40, 19, -20):
    hero.moveXY(80, y)
    hero.say("Here")

# Next with the south border (y = 20) from x = 60 to x = 20 with the step size of -20.
for x in range(60, 20, -20):
    hero.moveXY(x, 20)
    hero.say("Here")

# Next the west border (x = 20) from y = 40 to y = 60 with the step size of 20.
for y in range(40, 60, 20):
    hero.moveXY(20, y)
    hero.say("Here")

# Hide inside the village
hero.moveXY(50, 40)