def count_vowels(string):
    try:
        # Check if input is a string
        if not isinstance(string, str):
            raise TypeError("Input must be a string")

        # Count and return the number of vowels in the string
        vowels = "aeiouAEIOU"
        return sum([1 for char in string if char in vowels])
    except TypeError as e:
        print("Error:", e)