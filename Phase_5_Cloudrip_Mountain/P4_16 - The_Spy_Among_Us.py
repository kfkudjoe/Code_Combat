def letterInWord(word, letter):
    for i in range(len(word)):
        character = word[i]

        if character == letter:
            return True
    return False


spyletter = "z"
frineds = hero.findFriends()

for friend in friends:
    friendName = friend.id

    if letterInWord(friendName, spyLetter):
        hero.say(friendName, "is a spy")
    else:
        hero.say(friendName, "is a friend")