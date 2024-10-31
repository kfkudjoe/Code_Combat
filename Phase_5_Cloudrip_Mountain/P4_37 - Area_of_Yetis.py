# The chosen one can stun yetis with a shout.
chosen = hero.findFriends[0]

# The power of the shout is equal to the area of a circle.
radius = chosen.distanceTo(chosen.findNearestEnemy())

# The area of a circle can be calculated with the formula:
area = Math.PI * radius * radius

# Tell the area to the chosen one.
hero.say(area)

# Don't just stand there! Fight!
while True:
    enemy = hero.findNearestEnemy()

    if enemy:
        hero.cast("drain-life", enemy)
        