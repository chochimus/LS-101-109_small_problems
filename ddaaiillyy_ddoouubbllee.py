def crunch(string):
    result = ""
    if string:
        result = string[0]
    for i in range(1, len(string)):
        if string[i - 1] != string[i]:
            result += string[i]
    return result
        

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
