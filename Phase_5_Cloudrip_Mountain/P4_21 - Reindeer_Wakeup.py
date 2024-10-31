deerStatus = ['asleep', 'asleep', 'asleep', 'asleep', 'asleep']
friends = hero.findFriends()

for deerIndex in range(len(friends)):
    reindeer = frineds[deerIndex]

    if reindeer.pos.y > 30:
        deerStatus[deerIndex] = 'awake'
    pass

for statusIndex in range(len(deerStatus)):
    hero.say("Reindeer " + statusIndex + "is " + deerStatus[statusIndex])