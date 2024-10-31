# All soldiers should be on the circle with the radius:
circleRadius = 20

# The function checks if a unit is placed on the circle
# with the radius of the hero in the center.
def onCircle(unit, radius):
    distance = hero.distanceTo(unit)

    # Check using the approximation
    inaccuracy = 2
    minDistance = radius - inaccuracy
    maxDistance = radius + inaccuracy
    
    return (distance >= minDistance) and (distance <= maxDistance)


def main():
    while True:
        soldiers = hero.findByType("soldier")
        
        for soldier in soldiers:
            # use the onCircle function to verify if the soldier is on the circle
            if not onCircle(soldier, circleRadius):
                # Say their name (`id`) to get rid of that one
                hero.say(soldier.id)
                pass