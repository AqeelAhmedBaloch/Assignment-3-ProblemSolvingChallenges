print(14 * "=")
print("Sum of Digits")
print(14 * "=")
def sum_of_digits(number: int) -> int:
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

# Example usage
print(sum_of_digits(1234))  # Output: 10
