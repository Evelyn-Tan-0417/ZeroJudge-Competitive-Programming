"""
ZeroJudge Problem d442: 10591 - Happy Number
Problem Source: UVa10591

Problem Description:
A happy number is a number whose repeated digit-square sum eventually leads to 1.
An unhappy number is one that gets stuck in a cycle that does not include 1.

For example:
- 7 is happy: 7 → 49 → 97 → 130 → 10 → 1
- 2 is unhappy: 2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 (cycle)

Algorithm: Cycle Detection with Set Tracking
Time Complexity: O(k) where k is the length until cycle/convergence
Space Complexity: O(k) for storing seen numbers

Submission Result: AC (2.9s, 3.3MB)
Date: 2023-08-06 20:23
"""

def is_happy_number(num):
    """
    Determine if a number is happy using cycle detection
    
    Args:
        num: string representation of the number
    
    Returns:
        bool: True if happy, False if unhappy
    """
    seen_numbers = []  # Track all numbers we've encountered
    current = int(num)
    seen_numbers.append(current)
    
    while True:
        # Calculate sum of squares of digits
        digit_square_sum = 0
        num_str = str(current)
        
        for digit_char in num_str:
            digit = int(digit_char)
            digit_square_sum += digit ** 2
        
        current = digit_square_sum
        
        # Check if we reached 1 (happy number)
        if current == 1:
            return True
        
        # Check if we've seen this number before (cycle detected)
        if current in seen_numbers:
            return False
        
        # Add to seen numbers and continue
        seen_numbers.append(current)

def main():
    """
    Main execution function handling multiple test cases
    """
    x = int(input())  # Number of test cases
    
    for i in range(x):
        num = input().strip()
        original_num = int(num)
        
        if is_happy_number(num):
            print(f"Case #{i+1}: {original_num} is a Happy number.")
        else:
            print(f"Case #{i+1}: {original_num} is an Unhappy number.")

if __name__ == "__main__":
    main()

"""
Algorithm Analysis:

1. Cycle Detection Strategy:
   - Keep track of all numbers encountered in the sequence
   - If we see a number twice, we've found a cycle (unhappy)
   - If we reach 1, the number is happy

2. Mathematical Insight:
   - All sequences either reach 1 or enter a cycle
   - No sequence can grow indefinitely
   - Maximum possible sum for any single step is bounded

3. Implementation Details:
   - Use list to track seen numbers (allows checking membership)
   - Convert between string and integer as needed for digit processing
   - Handle multiple test cases with proper formatting

4. Complexity Considerations:
   - Time: O(k) where k is steps until convergence/cycle
   - Space: O(k) for storing the sequence
   - In practice, sequences are quite short for most numbers

Key Learning Points:
- Cycle detection in mathematical sequences
- String to digit conversion and processing
- Mathematical sequence analysis
- Proper formatting for competitive programming output
"""
