alphabet = "abcdefghijklmnopqrstuvwxyz"



def encode_letter(letter, change_position):
    
    # Find the position of the letter within the alphabet
    letter_position = alphabet.find(letter)
    
    # Calculate the position of the secret letter
    secret_position = letter_position + change_position

    # If the secret_position is past the letter z we need
    # to go back around to the beginning of the alphabet
    if secret_position >= 26:
        secret_position = secret_position - 26

    # Get the secret letter at the secret position within
    # the alphabet
    secret_letter = alphabet[secret_position]

    # Give this secret letter back to where we called the function
    return secret_letter



print("Secret letter for a + 1: ", encode_letter("a", 1))

print("Secret letter for d + 3: ", encode_letter("d", 3))

print("Secret letter for y + 4: ", encode_letter("y", 4))

print("Secret letter for p - 2: ", encode_letter("p", -2))
