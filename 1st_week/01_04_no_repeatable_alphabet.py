def find_not_repeating_first_character(string):
    count_repeating_character_array = [0] * 26
    char = '';

    for character in ''.join(reversed(string)):
        count_repeating_character_array[ord(character) - ord('a')] += 1
        if count_repeating_character_array[ord(character) - ord('a')] == 1:
            char = character
    return char




print(find_not_repeating_first_character("abadabac"))