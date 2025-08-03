def print_in_box(string):
    side1 = f"+-{"-"*len(string)}-+"
    empty_mid = f"| {" "*len(string)} |"
    mid = f"| {string} |"
    print(side1)
    print(empty_mid)
    print(mid)
    print(empty_mid)
    print(side1)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')