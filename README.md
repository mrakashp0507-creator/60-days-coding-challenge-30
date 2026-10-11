# Day 30 – Week 5 Sprint Challenge

## Overview

This project solves two medium-level algorithm problems using optimized approaches. It focuses on performance, complexity analysis, optimization decisions, and trade-offs.

## Battle 1: Longest Substring Without Repeating Characters

**Problem:** Find the longest substring that contains no repeated characters.

**Example**

- Input: `abcabcbb`
- Output: `abc`
- Length: `3`

**Optimized approach:** Sliding window + hash map.

**Complexity**

- Time: O(n) average
- Space: O(k), where k is the number of distinct characters tracked

**Why it scales:** The window moves forward through the string, avoiding repeated examination of all substrings.

**Trade-off:** The hash map requires extra memory but improves performance over repeated substring checks.

## Battle 2: Product of Array Except Self

**Problem:** Return an array where each element is the product of all other input elements, without using division.

**Example**

- Input:&#x20;
  \# Day 30 - Week 5 Sprint Challenge
  \# Problem 1: Longest Substring Without Repeating Characters
  \# Problem 2: Product of Array Except Self


  def longest_unique_substring(text):
  &#x20;   last_seen = {}
  &#x20;   left = 0
  &#x20;   longest = 0
  &#x20;   best_start = 0

  &#x20;   for right, character in enumerate(text):
  &#x20;       if character in last_seen and last_seen[character] >= left:
  &#x20;           left = last_seen[character] + 1

  &#x20;       last_seen[character] = right
  &#x20;       current_length = right - left + 1

  &#x20;       if current_length > longest:
  &#x20;           longest = current_length
  &#x20;           best_start = left

  &#x20;   substring = text[best_start\:best_start + longest]
  &#x20;   return longest, substring


  def product_except_self(numbers):
  &#x20;   size = len(numbers)
  &#x20;   result = [1] \* size

  &#x20;   \# First pass: store products of all elements to the left
  &#x20;   prefix = 1
  &#x20;   for i in range(size):
  &#x20;       result[i] = prefix
  &#x20;       prefix \*= numbers[i]

  &#x20;   \# Second pass: multiply by products of all elements to the right
  &#x20;   suffix = 1
  &#x20;   for i in range(size - 1, -1, -1):
  &#x20;       result[i] \*= suffix
  &#x20;       suffix \*= numbers[i]

  &#x20;   return result


  def main():
  &#x20;   print("=" \* 50)
  &#x20;   print("       WEEK 5 SPRINT CHALLENGE")
  &#x20;   print("=" \* 50)

  &#x20;   \# Problem 1
  &#x20;   print("\nBATTLE 1: Longest Unique Substring")
  &#x20;   text = input("Enter a string: ")

  &#x20;   length, substring = longest_unique_substring(text)

  &#x20;   print("Original string:", text)
  &#x20;   print("Longest substring:", repr(substring))
  &#x20;   print("Substring length:", length)

  &#x20;   \# Problem 2
  &#x20;   print("\nBATTLE 2: Product of Array Except Self")
  &#x20;   raw_numbers = input("Enter integers separated by spaces: ").strip()

  &#x20;   try:
  &#x20;       numbers = list(map(int, raw_numbers.split()))

  &#x20;       if not numbers:
  &#x20;           print("Please enter at least one integer.")
  &#x20;       else:
  &#x20;           result = product_except_self(numbers)
  &#x20;           print("Original array:", numbers)
  &#x20;           print("Product array: ", result)

  &#x20;   except ValueError:
  &#x20;       print("Invalid input. Please enter integers only.")

  &#x20;   print("\n" + "=" \* 50)
  &#x20;   print("SPRINT CHALLENGE COMPLETED!")
  &#x20;   print("=" \* 50)


  if \_\_name\_\_ == "\_\_main\_\_":
  &#x20;   main()

- Output: `[24, 12, 8, 6]`

**Optimized approach:** Prefix products followed by suffix products.

**Complexity**

- Time: O(n)
- Auxiliary space: O(1), excluding the output array

**Why it scales:** Two linear passes process the array efficiently, without nested loops or division.

**Trade-off:** The solution uses an output array to store results. Very large products may exceed the range of fixed-width integer types in some programming languages.

## Optimization Decisions

| Decision                 | Benefit                         | Trade-off                           |
| ------------------------ | ------------------------------- | ----------------------------------- |
| Sliding window           | Avoids checking every substring | Requires tracking window boundaries |
| Hash map                 | Fast character-index lookup     | Uses extra memory                   |
| Prefix and suffix passes | Linear-time product calculation | Requires two passes                 |
| No division              | Correctly supports zero values  | Requires prefix/suffix logic        |

## How to Run

1. Install Python 3.
2. Open the folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python day30_sprint_challenge.py
```

## Test Cases

### Battle 1

| Input        | Expected length |
| ------------ | --------------: |
| `abcabcbb`   |               3 |
| `bbbbb`      |               1 |
| `pwwkew`     |               3 |
| Empty string |               0 |

### Battle 2

| Input          | Expected output  |
| -------------- | ---------------- |
| `[1, 2, 3, 4]` | `[24, 12, 8, 6]` |
| `[0, 1, 2, 3]` | `[6, 0, 0, 0]`   |
| `[2, 3]`       | `[3, 2]`         |
| `[5]`          | `[1]`            |

## Learning Outcomes

- Applied sliding-window optimization.
- Used a hash map to track previous character positions.
- Applied prefix and suffix products.
- Analyzed time and space complexity.
- Explained the trade-offs between speed and memory usage.
