alphabet = "abcdefghijklmnopqrstuvwxyz"

def encode(letter, secret):
    pos = alphabet.find(letter)

    newpos = pos + secret

    if newpos >= 26:
        newpos = newpos - 26

    return alphabet[newpos]


def decode(letter, secret):
    pos = alphabet.find(letter)

    newpos = pos - secret

    if newpos < 0:
        newpos = newpos + 26

    return alphabet[newpos]



secret = 17
message = "yvccf nficu"
output = ""

for letter in message:
    if letter in alphabet:
        output = output + decode(letter, secret)
    else:
        output = output + letter

print(output)
