hero.moveXY(14, 24)

secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()
secretC = secretA and secretB

if secretC:
    hero.moveXY(20, 33)
else:
    hero.moveXY(20, 15)

hero.moveXY(26, 24)

secretD = secretA or secretB

if secretD:
    hero.moveXY(32, 33)

hero.moveXY(38, 24)

if not secretB:
    hero.moveXY(44, 33)
else:
    hero.moveXY(44, 15)

hero.moveXY(50, 24)