from dict import CHARACTERS

s = input(str("Let's write a word (in pt-BR, en-US or in morse code): "))

def morse(text):
    decrypt = {value: key for key,value in CHARACTERS.items()}

    if '-' in text:
        return ''.join(decrypt[item] for item in text.split())
    return ' '.join(CHARACTERS[item] for item in text.upper())


print(morse(s))
