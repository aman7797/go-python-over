from random import randint

# Random number generator
variable = randint(1,100)

# Warm Marker

# WARMER Marker

# COLD marker 

# COLDER market



print("Rules\n1. If a player's guess is less than 1 or greater than 100, say 'OUT OF BOUNDS'\n2. On a player's first turn, if their guess is\n * within 10 of the number, return 'WARM!'\n * further than 10 away from the number, return 'COLD!'\n3. On all subsequent turns, if a guess is \n * closer to the number than the previous guess return 'WARMER!'\n * farther from the number than the previous guess, return 'COLDER!'\n4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!")