"""
ZeroJudge Problem f312: 1. 人力分配 (Resource Allocation)
Problem Source: 2020年10月APCS

Problem Description:
Given n people to allocate between two projects with quadratic productivity functions,
find the allocation that maximizes total productivity.

Project A productivity: a₀×x² + a₁×x + a₂ (where x = people assigned to A)
Project B productivity: b₀×y² + b₁×y + b₂ (where y = people assigned to B)
Constraint: x + y = n (total people)

Algorithm: Exhaustive Search with Mathematical Optimization
Time Complexity: O(n)
Space Complexity: O(1)

Submission Result: AC (18ms, 3.3MB)
Date: 2023-05-28 19:58
"""

def calculate_productivity(coefficients, people):
    """
    Calculate productivity using quadratic function
    
    Args:
        coefficients: list [a₀, a₁, a₂] for function a₀x² + a₁x + a₂
        people: number of people assigned to this project
    
    Returns:
        int: productivity value
    """
    a0, a1, a2 = coefficients
    return a0 * people * people + a1 * people + a2

def find_optimal_allocation(project_a_coeffs, project_b_coeffs, total_people):
    """
    Find optimal allocation of people between two projects
    
    Args:
        project_a_coeffs: coefficients [a₀, a₁, a₂] for project A
        project_b_coeffs: coefficients [b₀, b₁, b₂] for project B
        total_people: total number of people to allocate
    
    Returns:
        int: maximum total productivity
    """
    max_productivity = 0
    
    # Try all possible allocations from 0 to n people for project A
    for people_a in range(total_people + 1):
        people_b = total_people - people_a
        
        # Calculate productivity for both projects
        productivity_a = calculate_productivity(project_a_coeffs, people_a)
        productivity_b = calculate_productivity(project_b_coeffs, people_b)
        
        total_productivity = productivity_a + productivity_b
        
        # Update maximum if this allocation is better
        if people_a == 0:  # Initialize with first calculation
            max_productivity = total_productivity
        elif total_productivity > max_productivity:
            max_productivity = total_productivity
    
    return max_productivity

def main():
    """
    Main execution function
    """
    # Read coefficients for project A
    project_a_coeffs = list(map(int, input().split()))
    
    # Read coefficients for project B
    project_b_coeffs = list(map(int, input().split()))
    
    # Read total number of people
    total_people = int(input())
    
    # Find and output optimal allocation
    result = find_optimal_allocation(project_a_coeffs, project_b_coeffs, total_people)
    print(result)

if __name__ == "__main__":
    main()

"""
Algorithm Analysis:

1. Problem Type: Constrained Optimization
   - Maximize: f_A(x) + f_B(y) 
   - Subject to: x + y = n, x ≥ 0, y ≥ 0
   - Where f_A and f_B are quadratic functions

2. Solution Strategy:
   - Since n is typically small in competitive programming
   - Exhaustive search over all valid allocations is feasible
   - For each allocation (x, n-x), calculate total productivity

3. Mathematical Insight:
   - Quadratic functions can have maximum/minimum points
   - Discrete optimization over integer allocations
   - Could be solved analytically with calculus, but brute force is simpler

4. Implementation Details:
   - Evaluate quadratic function: ax² + bx + c
   - Iterate through all possible values of x from 0 to n
   - Track maximum productivity seen

5. Optimization Potential:
   - Could use calculus to find analytical optimum
   - But discrete constraint requires checking integer points anyway
   - Current O(n) solution is optimal for this constraint

Key Learning Points:
- Quadratic function evaluation and optimization
- Constrained optimization with discrete variables
- Exhaustive search when solution space is small
- Mathematical modeling of resource allocation problems
"""
