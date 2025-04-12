print(12 * "=")
print("Count Vowels")  # Output: 3
print(12 * "=")
def count_vowels(input_str: str) -> int:
    vowels = set("aeiou")
    count = 0
    for char in input_str.lower():
        if char in vowels:
            count += 1
    return count

# Example usage
print(count_vowels("Apple"))  # Output: 2
