def century(year):
    century = year // 100 + 1
    if year % 100 == 0:
        century -= 1
    
    suffix = century_suffix(century)
    return f'{century}{suffix}'

def century_suffix(year):
    last_two = year % 100
    last_digit = year % 10

    match last_two:
        case 11 | 12 | 13:
            return 'th'
    
    match last_digit:
        case 1:
            return 'st'
        case 2:
            return 'nd'
        case 3:
            return 'rd'
        case _:
            return 'th'
        

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")  
