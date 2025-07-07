"""
ZeroJudge Problem j608: 4. 機器出租 (Machine Rental)
Problem Source: 2023年1月APCS

Problem Description:
Given n rental requests with start/end times and k machines available,
maximize the number of requests that can be fulfilled.

Algorithm: Greedy Algorithm with Binary Search Optimization
Time Complexity: O(n log n + n log k)
Space Complexity: O(n + k)

Submission Result: AC (0.4s, 32.1MB)
Date: 2024-03-31 20:25
"""

import bisect

def solve_machine_rental():
    """
    Solve machine rental optimization problem using greedy approach
    
    Strategy:
    1. Sort requests by end time (earliest end first)
    2. For each request, assign to earliest available machine
    3. Use binary search for efficient machine selection
    
    Returns:
        int: maximum number of requests that can be fulfilled
    """
    # Read input
    n, k = map(int, input().split())  # n = requests, k = machines
    start_times = list(map(int, input().split()))
    end_times = list(map(int, input().split()))
    
    # Create list of (start_time, end_time) tuples
    requests = []
    for i in range(n):
        requests.append((start_times[i], end_times[i]))
    
    # Sort by end time (greedy choice: handle earliest ending requests first)
    requests.sort(key=lambda x: x[1])
    
    # Track when each machine becomes available
    # Initialize all machines as available at time -1
    machine_availability = [-1] * k
    
    fulfilled_count = 0
    
    for start_time, end_time in requests:
        # Find the machine that becomes available earliest
        # but before or at the start time of current request
        
        # Find the position where we could insert start_time
        # All machines at positions before this are available
        insert_pos = bisect.bisect_left(machine_availability, start_time)
        
        if insert_pos > 0:
            # We can assign this request to a machine
            # Remove the earliest available machine
            machine_availability.pop(insert_pos - 1)
            
            # Add the machine back with its new availability time (end_time)
            bisect.insort(machine_availability, end_time)
            
            fulfilled_count += 1
    
    return fulfilled_count

# Main execution
def main():
    result = solve_machine_rental()
    print(result)

if __name__ == "__main__":
    main()

"""
Algorithm Analysis:

1. Greedy Strategy:
   - Process requests in order of end time
   - Always choose the machine that becomes available earliest
   - This maximizes future opportunities

2. Binary Search Optimization:
   - bisect_left(): O(log k) to find insertion point
   - insort(): O(log k) for insertion in sorted order
   - This avoids O(k) linear search through machines

3. Key Insights:
   - Sorting by end time is crucial for optimal solution
   - Maintaining sorted machine availability enables binary search
   - Greedy choice is optimal due to exchange argument

4. Time Complexity Breakdown:
   - Sorting requests: O(n log n)
   - For each request: O(log k) for binary search operations
   - Total: O(n log n + n log k)

Alternative Approaches Considered:
- Brute force: O(n! * k) - exponential, impractical
- Dynamic programming: O(n * k * max_time) - too slow for large inputs
- This greedy approach: optimal and efficient
"""
