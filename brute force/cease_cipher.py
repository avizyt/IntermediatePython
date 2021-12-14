code_msg = 'nzohfu gur rarzl ng avtug'

for counter in range(26):
    guessedMessage = ''

    for x in code_msg:
        if x != ' ':
            if ord(x) + counter <= 122:
                x = chr(ord(x) + counter)
        else:
            x = chr(ord(x) + counter-26)
        guessedMessage += x

    print(counter,guessedMessage)