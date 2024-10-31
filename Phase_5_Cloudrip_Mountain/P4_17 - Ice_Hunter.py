def isSubstring(word, substring):
    """
    This function checks if a word contains a substring,
    """

    # Iterate through the start indexes only.
    rightEdge = len(word) - len(substring)

    # Loop through the indexes of the word.
    for i in range(rightEdge + 1):

        # For each index, loop through the substring.
        for j in range(len(substring)):

            # Use an offset for the word's indexes
            shiftedIndex = i + j

            # If letters aren't the same
            if word[shiftedIndex] != substring[j]:
                # Check the next start index in the word.
                break
            
            # If it was the last letter in the substring:
            if j == len(substring) - 1:
                return True
    
    # Substring does not exit in the word.
    return False


enemies = hero.findEnemies()

# Loop through all enemies.
for e in range(len(enemies)):
    enemy = enemies[e]

    # Check if enemy.id contains "bos" using is Substring
    if isSubstring(enemy.id, "bos"):
        while enemy.health > 0:
            hero.cast("drain-life", enemy)