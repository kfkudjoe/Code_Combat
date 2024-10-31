while True:
    flagGreen = hero.findFlag("green")
    flagBlack = hero.findFlag("black")

    if flagGreen:
        hero.buildXY("fence", flagGreen.pos.x, flagGreen.pos.y)
        hero.pickUpFlag(flagGreen)
    elif flagBlack:
        hero.buildXY("fire-trap", flagBlack.pos.x, flagBlack.pos.y)
        hero.pickUpFlag(flagBlack)

    hero.moveXY(43, 31)