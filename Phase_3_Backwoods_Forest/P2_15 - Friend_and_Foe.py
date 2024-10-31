while True:
    friend = hero.findNearestFriend()
    if friend:
        hero.say("To battle, " + friend.id + "!")
    
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.say("You shall not pass!" + enemy + "Go away!")