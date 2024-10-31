def chooseStrategy():
    enemy = hero.findNearestEnemy()

    # If you can summon a griffin-rider, return griffin-rider
    if hero.gold > hero.costOf("griffin-rider"):
        return "griffin-rider"
    # If there is a fangirder on your side of the mines, return "fight-back"
    if enemy and enemy.pos.x < 50:
        return "fight-back"
    # Otherwise, return "collect-coins":
    else:
        return "collect-coins"

def commandAttack():
    # Command your griffin-riders to attack ogres.
    griffinRiders = hero.findByType("griffin-rider")
    enemies = hero.findEnemies()
    attackIndex = 0

    while attackIndex < len(griffinRiders):
        griffinRider = griffinRiders[attackIndex]
        enemy = enemies[attackIndex]
        attackIndex += 1

        if griffinRider and enemy:
            hero.command(griffinRider, "attack", enemy)

def pickUpCoin():
    # Collect coins
    coin = hero.findNearestItem()

    if coin:
        hero.move(coin.pos)

def heroAttack():
    enemy= hero.findNearestEnemy()

    if enemy.pos.x < 50:
        hero.cast("drain-life", enemy)

def main():
    while True:
        commandAttack()
        strategy = chooseStrategy()

        # Call a function, depending on what the current strategy is.
        if strategy == "griffin-rider":
            hero.summon("griffin-rider")
        elif strategy == "fight-back":
            heroAttack()
        elif strategy == "collect-coins":
            pickUpCoin()

        if hero.time > 30:
            if hero.canCast("summon-yeti"):
                hero.cast("summon-yeti")
            if hero.canCast("summon-burl"):
                hero.cast("summon-burl")
            if hero.canCast("raise-dead"):
                hero.cast("raise-dead")


main()