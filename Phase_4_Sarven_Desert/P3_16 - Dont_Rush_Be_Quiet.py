# Move slow along a pattern

# This function returns a value from 0 to 30 (0 <= n < 30)
def mod30(n):
    if n >= 30:
        return n - 30
    else:
        return n

# This function should return a value from 0 to 40 (0 <= n < 40)
def mod40(n):
    if n >= 40:
        return n - 40
    else:
        return n


while True:
    time = hero.time
    x = mod30(time) + 25
    y = mod40(time) + 10

    hero.moveXY(x, y)