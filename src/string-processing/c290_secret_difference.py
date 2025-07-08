"""
ZeroJudge Problem c290: APCS 2017-0304-1秘密差 (Secret Difference)
Problem Source: 2017年3月APCS

Problem Description:
Calculate the absolute difference between:
- Sum of digits at even positions (1st, 3rd, 5th, ...)
- Sum of digits at odd positions (2nd, 4th, 6th, ...)

Note: Positions are 1-indexed, so "even positions" means 1st, 3rd, 5th...
which correspond to indices 0, 2, 4... (0-indexed)

Algorithm: String Indexing with Mathematical Calculation
Time Complexity: O(n) where n is string length
Space Complexity: O(n) for digit storage

Submission Result: AC (16ms, 3.3MB)
Date: 2022-07-29 10:55
"""

def calculate_secret_difference(number_string):
    """
    Calculate secret difference between alternating digit sums
    
    Args:
        number_string: string representation of the number
    
    Returns:
        int: absolute difference between even and odd position sums
    """
    # Convert string to list of integers for easier processing
    digits = [int(digit_char) for digit_char in number_string]
    
    even_position_sum = 0  # Sum of digits at positions 1, 3, 5, ... (indices 0, 2, 4, ...)
    odd_position_sum = 0   # Sum of digits at positions 2, 4, 6, ... (indices 1, 3, 5, ...)
    
    # Process each digit based on its position
    for i in range(len(digits)):
        if i % 2 == 0:
            # Even index = odd position number (1st, 3rd, 5th, ...)
            even_position_sum += digits[i]
        else:
            # Odd index = even position number (2nd, 4th, 6th, ...)
            odd_position_sum += digits[i]
    
    # Calculate absolute difference
    secret_difference = abs(even_position_sum - odd_position_sum)
    return secret_difference

def main():
    """
    Main execution function
    """
    # Read the number as a string to preserve leading zeros and handle large numbers
    number_string = input().strip()
    
    # Calculate and output the secret difference
    result = calculate_secret_difference(number_string)
    print(result)

if __name__ == "__main__":
    main()

"""
Algorithm Analysis:

1. Problem Interpretation:
   - "Even positions" in problem statement means 1st, 3rd, 5th... positions
   - In 0-indexed arrays, these correspond to indices 0, 2, 4...
   - "Odd positions" means 2nd, 4th, 6th... positions (indices 1, 3, 5...)

2. Algorithm Strategy:
   - Convert string to list of individual digits
   - Use modular arithmetic to determine position type
   - Accumulate sums for each position type
   - Calculate absolute difference

3. Implementation Details:
   - List comprehension for string-to-digit conversion
   - Modulo operation (i % 2) for position classification
   - Separate accumulators for even/odd position sums
   - abs() function for final difference calculation

4. Index vs Position Mapping:
   - Index 0 (1st position) → even_position_sum
   - Index 1 (2nd position) → odd_position_sum  
   - Index 2 (3rd position) → even_position_sum
   - Index 3 (4th position) → odd_position_sum
   - Pattern: index % 2 == 0 → even position in 1-indexed counting

5. Edge Cases:
   - Single digit numbers (only even position sum)
   - Numbers with leading zeros (handled by string input)
   - Large numbers (string processing avoids integer overflow)

6. Mathematical Insight:
   - Alternating sum calculation
   - Absolute value ensures non-negative result
   - Modular arithmetic for pattern recognition

Key Learning Points:
- String to digit conversion techniques
- Index vs position number mapping (0-indexed vs 1-indexed)
- Modular arithmetic for alternating patterns
- List comprehension for data transformation
- Absolute difference calculations
"""
