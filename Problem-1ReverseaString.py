print(17 * "=")
print("Reverse a String")  # Output: "dlrow"
print(17 * "=")

def reverse_string(input_str: str) -> str:
    return input_str[::-1]

# Example usage
print(reverse_string("hello"))  # Output: "olleh"
