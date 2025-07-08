"""
ZeroJudge Problem f605: 1. 購買力 (Purchasing Power)
Problem Source: 2021年1月APCS

Problem Description:
Given n stores with m prices each, calculate purchasing power based on:
- A store is "valid" if max_price - min_price >= d (threshold)
- Total purchasing power = sum of (average prices of valid stores)
- Output: count of valid stores and total purchasing power

Algorithm: Statistical Analysis with Conditional Logic
Time Complexity: O(n×m)
Space Complexity: O(m) for storing prices per store

Submission Result: AC (22ms, 3.3MB)
Date: 2023-05-28 19:49
"""

def analyze_store_purchasing_power(prices, threshold):
    """
    Analyze a single store's purchasing power
    
    Args:
        prices: list of prices in the store
        threshold: minimum price difference required (d)
    
    Returns:
        tuple: (is_valid, purchasing_power)
               is_valid: True if store meets threshold criteria
               purchasing_power: average price if valid, 0 if invalid
    """
    max_price = max(prices)
    min_price = min(prices)
    price_difference = max_price - min_price
    
    # Check if store meets threshold requirement
    if price_difference >= threshold:
        # Store is valid, calculate purchasing power (average price ÷ 3)
        total_price = sum(prices)
        purchasing_power = total_price // 3  # Integer division as per problem
        return True, purchasing_power
    else:
        # Store doesn't meet threshold
        return False, 0

def main():
    """
    Main execution function
    """
    # Read n (number of stores) and d (threshold)
    n, d = map(int, input().split())
    
    valid_store_count = 0
    total_purchasing_power = 0
    
    # Process each store
    for i in range(n):
        # Read prices for current store
        prices = list(map(int, input().split()))
        
        # Analyze this store
        is_valid, purchasing_power = analyze_store_purchasing_power(prices, d)
        
        if is_valid:
            valid_store_count += 1
            total_purchasing_power += purchasing_power
    
    # Output results
    print(valid_store_count, total_purchasing_power)

if __name__ == "__main__":
    main()

"""
Algorithm Analysis:

1. Problem Breakdown:
   - For each store: analyze m prices
   - Condition: max_price - min_price >= threshold
   - If valid: purchasing_power = sum(prices) // 3
   - Output: count of valid stores and sum of their purchasing powers

2. Statistical Operations per Store:
   - max(prices): O(m) to find maximum price
   - min(prices): O(m) to find minimum price
   - sum(prices): O(m) to calculate total
   - Overall per store: O(m)

3. Algorithm Flow:
   - Initialize counters for valid stores and total purchasing power
   - For each store:
     * Calculate price statistics
     * Check validity condition
     * Update counters if valid
   - Output final results

4. Implementation Details:
   - Use built-in max(), min(), sum() functions for clarity
   - Integer division (//) as specified in problem
   - Clear separation of store analysis logic
   - Accumulate results across all stores

5. Edge Cases Handled:
   - Stores with identical prices (difference = 0)
   - Single-item stores (valid if meets threshold)
   - All invalid stores (output: 0 0)

Key Learning Points:
- Statistical analysis of data sets (max, min, average)
- Conditional aggregation based on criteria
- Efficient use of Python built-in functions
- Clear separation of concerns in algorithm design
- Integer arithmetic in competitive programming
"""
