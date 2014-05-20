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

print(encode("a", 17))
print(decode("r", 17))
