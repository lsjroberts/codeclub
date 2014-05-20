# List of letters in alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Secret letter to decode
letter = "r"

# Secret used to decode the letter
secret = 17

# Find the position of the secret letter, this will
# be a number between 0 and 25
secret_position = alphabet.find(letter)

# Count backward from this position
letter_position = secret_position - secret

# If we count too far, loop back around
if letter_position < 0:
    letter_position = letter_position + 26

# Now we look up the letter at this secret position
letter = alphabet[letter_position]

# Output the secret letter to the screen
print(letter)
