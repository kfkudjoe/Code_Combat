while True:
    friends = hero.findFriends()
    skeletons = hero.findByType('skeleton')

    if hero.canCast("summon-undead") and len(skeletons) < 4:
        hero.cast("summon-undead")
    
    if hero.time < 15:
        for skeleton in skeletons[:2]:
            skeletonEnemy = skeleton.findNearestEnemy()

            if skeletonEnemy:
                hero.command(skeleton, 'attack', skeletonEnemy)
            else:
                hero.command(skeleton, 'move', {'x': 60, 'y': 67})
        
        heroEnemy = hero.findNearestEnemy()
        hero.moveXY(82, 49)

        if heroEnemy:
            hero.cast("drain-life", heroEnemy)

    elif hero.time > 15:
        for friend in friends:
            xPos = friend.pos.x
            yPos = friend.pos.y
            friendEnemy = friend.findNearestEnemy()

            if friendEnemy:
                hero.command(friend, 'attack', friendEnemy)
            else:
                hero.command(frined, 'move', {'x': xPos, 'y': yPos})