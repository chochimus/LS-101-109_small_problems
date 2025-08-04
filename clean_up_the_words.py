def clean_up(string):
    clean_text = ''

    for char in string:
        if char.isalpha():
            clean_text += char
        elif not clean_text or clean_text[-1] != ' ':
            clean_text += ' '

    return clean_text

print(clean_up("---what's my +*& line?") == " what s my line ")
# True