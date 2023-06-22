def compare_strings(string1, string2):
    # Ensure the strings have the same length
    if len(string1) != len(string2):
        return False

    # Compare character by character
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            return False

    return True

# Example usage
str1 = "Hello"
str2 = "Hxllo"
if compare_strings(str1, str2):
    print("The strings match!")
else:
    print("The strings do not match.")
