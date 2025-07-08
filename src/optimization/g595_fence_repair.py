"""
ZeroJudge Problem g595: 1. 修補圍籬 (Fence Repair)
Problem Source: 2021年11月APCS

Problem Description:
Given n fence segments with heights, calculate the minimum cost to repair segments
with height 0. The repair cost for a segment is the minimum height of its neighbors.

For boundary segments (first and last):
- First segment: use only right neighbor
- Last segment: use only left neighbor
- Middle segments: use minimum of left and right neighbors

Algorithm: Array Processing with Boundary Handling
Time Complexity: O(n)
Space Complexity: O(n) for input storage

Submission Result: AC (18ms, 3.3MB)
Date: 2023-05-28 19:40
"""

def calculate_repair_cost(fence_heights):
    """
    Calculate total repair cost for fence segments
    
    Args:
        fence_heights: list of integers representing fence heights
                      (0 = needs repair, >0 = current height)
    
    Returns:
        int: total repair cost
    """
    n = len(fence_heights)
    total_cost = 0
    
    for i in range(n):
        # Only process segments that need repair (height = 0)
        if fence_heights[i] == 0:
            
            if i == 0:
                # First segment: use right neighbor's height
                repair_cost = fence_heights[1]
                
            elif i == n - 1:
                # Last segment: use left neighbor's height
                repair_cost = fence_heights[n - 2]
                
            else:
                # Middle segment: use minimum of both neighbors
                left_height = fence_heights[i - 1]
                right_height = fence_heights[i + 1]
                repair_cost = min(left_height, right_height)
            
            total_cost += repair_cost
    
    return total_cost

def main():
    """
    Main execution function
    """
    # Read number of fence segments
    n = int(input())
    
    # Read fence heights
    fence_heights = list(map(int, input().split()))
    
    # Calculate and output total repair cost
    total_cost = calculate_repair_cost(fence_heights)
    print(total_cost)

if __name__ == "__main__":
    main()

"""
Algorithm Analysis:

1. Problem Classification:
   - Array processing with conditional logic
   - Boundary condition handling
   - Optimization: minimize repair cost per segment

2. Repair Cost Rules:
   - Segment 0 (first): cost = height[1]
   - Segment n-1 (last): cost = height[n-2] 
   - Segment i (middle): cost = min(height[i-1], height[i+2])
   - Only apply to segments with height = 0

3. Algorithm Strategy:
   - Single pass through array: O(n)
   - For each zero-height segment, calculate optimal repair cost
   - Handle boundary cases separately from middle cases
   - Accumulate total cost

4. Implementation Details:
   - Clear boundary condition handling
   - Use of min() function for middle segments
   - Direct array indexing with bounds checking
   - Separation of concerns: cost calculation vs main logic

5. Edge Cases:
   - Single segment (no neighbors - problem constraint ensures n ≥ 2)
   - All segments need repair
   - No segments need repair (all heights > 0)
   - Adjacent zero segments

6. Optimization Insight:
   - Greedy approach: each segment repaired independently
   - Local optimization leads to global optimum
   - No interaction effects between repair decisions

Key Learning Points:
- Array boundary condition handling
- Conditional processing based on array values
- Index-based neighbor access patterns
- Greedy optimization in local decision problems
- Clean separation of edge cases and normal cases
"""
