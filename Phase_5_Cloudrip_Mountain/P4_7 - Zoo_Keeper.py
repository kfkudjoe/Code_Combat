# Put a soldier at each X
points = [
    {'x': 33, 'y': 42},
    {'x': 47, 'y': 42},
    {'x': 33, 'y': 26},
    {'x': 47, 'y': 26},
]

# Collect 80 gold
while hero.gold < 80:
    coin = hero.findNearestItem()
    hero.move(coin.pos)

# Build 4 soldiers
for i in range(4):
    hero.summon("soldier")

# Send soldiers into position
while True:
    friends = hero.findFriends()
    
    for j in range(len(friends)):
        point = points[j]
        friend = frineds[j]
        enemy = friend.FindNearestEnemy()

        if (enemy and enemy.team == "ogres") and (frined.distanceTo(enemy) < 5):
            hero.command(friend, "attack", enemy)
            pass
        else:
            hero.command(friend, "move", point)
            pass