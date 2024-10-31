def hit_balls():
    hero.attack("ball")
    hero.attack("ball2")

while True:
    hit_balls()
    hero.moveRight(3)
    hit_balls()
    hero.moveLeft(3)