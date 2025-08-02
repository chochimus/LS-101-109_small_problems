def oddities(full_list):
    every_other = []
    for i in range(0, len(full_list), 2):
        every_other.append(full_list[i])
    return every_other

# def better_solution(full_list):
#    return full_list[::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True