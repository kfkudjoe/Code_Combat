while True:
    enemies = hero.findEnemies()
    skeletons = hero.findByType("skeleton", hero.findFriends())

    if hero.canCast("summon-undead"):
        hero.cast("summon-undead"):
        [ hero.command(skeleton, "defend", hero) for skeleton in skeletons ]
    
    for enemy in enemies:
        distance = hero.distanceTo(enemy)

        if distance < 10:
            hero.cast("drain-life", enemy)

            if hero.canCast("fear"):
                [ hero.cast("fear", enemy) for enemy in enemies ]

    for enemy in enemies:
        if hero.canCast("chain-lightning"):
            hero.cast("chain-lightning", enemy)
        elif hero.canCast("poison-cloud"):
            hero.cast("poison-cloud", enemy)

    if (hero.canCast("raise-dead")) and (hero.findCorpses()):
        hero.cast("raise-dead")