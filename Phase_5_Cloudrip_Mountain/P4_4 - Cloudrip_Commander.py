while hero.gold > hero.costOf("soldier"):
    hero.summon("soldier")

soldiers = hero.findFriends()
soldierIndex = 0

while soldierIndex < len(soldiers):
    soldier = soldiers[soldierIndex]
    soldierIndex += 1
    hero.command(soldier, "move", {'x': 50, 'y': 40})

hero.moveXY(50, 40)