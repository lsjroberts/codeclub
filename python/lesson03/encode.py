# List of letters in alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Letter to encode
letter = "a"

# Secret used to encode the letter
secret = 3

# Find the position of the letter, this will
# be a number between 0 and 25
letter_position = alphabet.find(letter)

# Count forward from this position
secret_position = letter_position + secret

# If we count too far we'll have to start from the beginning
if secret_position >= 26:
    secret_position = secret_position - 26

# Now we look up the letter at this secret position
secret_letter = alphabet[secret_position]

# Output the secret letter to the screen
print(secret_letter)
