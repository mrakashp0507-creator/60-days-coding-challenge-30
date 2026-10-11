
# Day 30 - Week 5 Sprint Challenge
# Problem 1: Longest Substring Without Repeating Characters
# Problem 2: Product of Array Except Self


def longest_unique_substring(text):
    last_seen = {}
    left = 0
    longest = 0
    best_start = 0

    for right, character in enumerate(text):
        if character in last_seen and last_seen[character] >= left:
            left = last_seen[character] + 1

        last_seen[character] = right
        current_length = right - left + 1

        if current_length > longest:
            longest = current_length
            best_start = left

    substring = text[best_start:best_start + longest]
    return longest, substring


def product_except_self(numbers):
    size = len(numbers)
    result = [1] * size

    # First pass: store products of all elements to the left
    prefix = 1
    for i in range(size):
        result[i] = prefix
        prefix *= numbers[i]

    # Second pass: multiply by products of all elements to the right
    suffix = 1
    for i in range(size - 1, -1, -1):
        result[i] *= suffix
        suffix *= numbers[i]

    return result


def main():
    print("=" * 50)
    print("       WEEK 5 SPRINT CHALLENGE")
    print("=" * 50)

    # Problem 1
    print("\nBATTLE 1: Longest Unique Substring")
    text = input("Enter a string: ")

    length, substring = longest_unique_substring(text)

    print("Original string:", text)
    print("Longest substring:", repr(substring))
    print("Substring length:", length)

    # Problem 2
    print("\nBATTLE 2: Product of Array Except Self")
    raw_numbers = input("Enter integers separated by spaces: ").strip()

    try:
        numbers = list(map(int, raw_numbers.split()))

        if not numbers:
            print("Please enter at least one integer.")
        else:
            result = product_except_self(numbers)
            print("Original array:", numbers)
            print("Product array: ", result)

    except ValueError:
        print("Invalid input. Please enter integers only.")

    print("\n" + "=" * 50)
    print("SPRINT CHALLENGE COMPLETED!")
    print("=" * 50)


if __name__ == "__main__":
    main()
