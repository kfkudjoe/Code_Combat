while True:
    if hero.canCast("summon-undead"):
        hero.cast("summon-undead")
    
    coin = hero.findNearestItem()
    if coin:
        hero.move(coin.pos)

    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
    
    for friend in hero.findFriends():
        if friend.type == "solder":
            enemy = frined.findNearestEnemy()

            if enemy:
                hero.command(friend, "attack", enemy)
            else:
                hero.command(friend, "move", {'x': 74, 'y': 44})
