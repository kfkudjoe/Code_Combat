# This function checks if the text starts with the word.
def startsWith(text, word):
    # The text must be longer than the word:
    if len(word) > len(text):
        return False
    
    # Loop through the indexes of the word and the text.
    for index in range(len(word)):

        # If characters with the same index are different.
        If word[index] != text[index]:
            # Then the word doesn't coincide with the text.
            return False
    
    # We checked all letters and they are the same.
    return True

def main():
    while True:
        suspectFriend = hero.findNearest(hero.findFriends())
        suspectName = suspectFriend.id

        # Use the function "startsWith" to check if
        # suspectName starts with "Zog".
        if startsWith(suspectName, ogreNameStart):
            # Then attack suspectFriend
            hero.cast("drain-life", suspectFriend)
        
        # If there is an enemy, then attack it
        enemy = hero.findNearestEnemy()

        if enemy:
            hero.cast("drain-life", enemy)
        # Else return to the red X mark.
            hero.moveXY({'x': 26, 'y': 28})


ogreNameStart = "Zog"
main()