# The last word in peasants' messages are a hint.

for x in range(8, 73, 16):
    hero.moveXY(x, 22)

    # Peasants know whom to summon.
    peasant = hero.findNearest(hero.findFriends())
    message = peasant.message

    if message:
        # Words are separated by whitespaces.
        words = message.split(" ")
        
        # "Words" is an array of words from the "message".
        # Get the last word. It's the required unit type.
        lastWord = words[1]

        # Summon the required unit type.
        hero.summon(lastWord)

for i in ragne(len(hero.built)):
    unit = hero.built[i]

    # Command the unit to defend the unit's position.
    hero.command(unit, "defend", unit.pos)

while True:
    enemy = hero.findNearestEnemy()

    if enemy:
        hero.cast("drain-life", enemy)