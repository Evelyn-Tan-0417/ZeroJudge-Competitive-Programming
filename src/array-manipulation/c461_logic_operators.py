"""
ZeroJudge Problem c461: APCS 邏輯運算子 (Logic Operators)
Problem Source: APCS

Problem Description:
Given three integers a, b, c, determine which logical operators produce c as output.
Test AND, OR, and XOR operations with boolean conversion.

Boolean conversion: 0 → False, any non-zero → True
Operations to test:
- AND: a AND b = c
- OR: a OR b = c  
- XOR: a XOR b = c (exclusive OR)

Output all valid operators, or "IMPOSSIBLE" if none work.

Algorithm: Boolean Logic Evaluation
Time Complexity: O(1)
Space Complexity: O(1)

Submission Result: AC (16ms, 3.3MB)
Date: 2022-07-30 10:07
"""

def convert_to_boolean(value):
    """
    Convert integer to boolean using competitive programming rules
    
    Args:
        value: integer input
    
    Returns:
        int: 1 if value != 0, 0 if value == 0
    """
    return 1 if value != 0 else 0

def test_logic_operators(a, b, c):
    """
    Test which logical operators produce the correct output
    
    Args:
        a, b, c: input integers
    
    Returns:
        list: list of valid operator names
    """
    # Convert inputs to boolean values (0 or 1)
    bool_a = convert_to_boolean(a)
    bool_b = convert_to_boolean(b)
    bool_c = convert_to_boolean(c)
    
    valid_operators = []
    
    # Test AND operation
    and_result = bool_a and bool_b
    if and_result == bool_c:
        valid_operators.append("AND")
    
    # Test OR operation
    or_result = bool_a or bool_b
    if or_result == bool_c:
        valid_operators.append("OR")
    
    # Test XOR operation
    # XOR: True if exactly one operand is True
    xor_result = abs(bool_a - bool_b)  # Equivalent to bool_a XOR bool_b
    if xor_result == bool_c:
        valid_operators.append("XOR")
    
    return valid_operators

def main():
    """
    Main execution function
    """
    # Read input values
    a, b, c = map(int, input().split())
    
    # Test all logical operators
    valid_operators = test_logic_operators(a, b, c)
    
    # Output results
    if len(valid_operators) == 0:
        print("IMPOSSIBLE")
    else:
        for operator in valid_operators:
            print(operator)

if __name__ == "__main__":
    main()

"""
Algorithm Analysis:

1. Boolean Logic Foundations:
   - Truth table evaluation for basic logical operators
   - Non-zero values treated as True (1)
   - Zero values treated as False (0)

2. Logical Operators Tested:
   - AND: Both operands must be True
   - OR: At least one operand must be True  
   - XOR: Exactly one operand must be True

3. XOR Implementation:
   - Standard: bool_a XOR bool_b
   - Alternative: abs(bool_a - bool_b)
   - Both give same result for boolean values

4. Truth Tables:
   AND: 0&0=0, 0&1=0, 1&0=0, 1&1=1
   OR:  0|0=0, 0|1=1, 1|0=1, 1|1=1
   XOR: 0^0=0, 0^1=1, 1^0=1, 1^1=0

5. Algorithm Flow:
   - Convert all inputs to boolean representation
   - Test each operator against expected output
   - Collect all valid operators
   - Output results or "IMPOSSIBLE"

6. Implementation Details:
   - Clear boolean conversion function
   - Separate testing logic for each operator
   - List accumulation for multiple valid answers
   - Proper output formatting

7. Digital Logic Application:
   - Logic gate simulation
   - Truth table verification
   - Boolean algebra implementation
   - Digital circuit analysis

Key Learning Points:
- Boolean algebra and logic gates
- Truth table evaluation in code
- Integer to boolean conversion rules
- Multiple solution handling
- Digital logic simulation
- Fundamental computer science concepts (logic circuits)
"""
