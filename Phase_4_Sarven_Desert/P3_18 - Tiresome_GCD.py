friends = hero.findFriends()
number1 = friends[0].secretNumber
number2 = friends[1].secretNumber

if number2 > number1:
    swap = number1
    number1 = number2
    number2 = swap


# Inefficient way to find GCD
def bruteforceGCD(a, b):
    hero.say("The naive algorithm")
    cycles = 0
    counter = b

    # Enumerate all possible divisors
    while True:
        cycles += 1

        if cycles > 100:
            hero.say("Calculating is hard. I'm tired")
            break
        
        # If both number have "counter" divisor
        if (a % counter == 0) and (b % counter == 0):
            break

        counter -= 1
    
    hero.say("I used" + cycles + " cycles")
    return counter


# It's smart way to find gcd
def euclideanGCD(a, b):
    cycles = 0

    while b:
        cycles += 1
        swap = b
        b = a % b
        a = swap
    
    hero.say("I used" + cycles + " cycles")
    return a


secretNumber = euclideanGCD(number1, number2)

hero.moveXY(48, 34)
hero.say(secretNumber)
hero.moveXY(68, 34)