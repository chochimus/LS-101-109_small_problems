def madlib():
    noun = get_word("Enter a noun: ")
    verb = get_word("Enter a verb: ")
    adjective = get_word("Enter an adjective: ")
    adverb = get_word("Enter an adverb: ")

    print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")
    print(f"The {adjective} {noun} {verb}s {adverb} over the lazy dog.")
    print(f"The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.")

def get_word(prompt):
    return input(prompt)

madlib()