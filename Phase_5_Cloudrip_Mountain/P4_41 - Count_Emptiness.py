
# Count the whitespace on both sides of a riddle.

# This function moves the hero N steps to the right.
def moveNSteps(n):
    hero.moveXY(hero.pos.x + 8 * n, hero.pos.y)

# Read the riddle.
riddle = hero.findNearestEnemy().riddle

# Trim whitespace from both sides and store in a variable.
trimmed = riddle.trim()

# Find the difference beween the `riddle` and `trimmed` lengths:
difference (riddle) - len(trimmed)

# Use the result and moveNSteps function to move to the spot.
moveNSteps(difference)

# Say something there!
hero.say("here!")