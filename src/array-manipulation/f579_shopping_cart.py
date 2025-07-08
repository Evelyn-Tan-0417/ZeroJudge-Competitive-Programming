"""
ZeroJudge Problem f579: 1. 購物車 (Shopping Cart)
Problem Source: 2020年7月APCS

Problem Description:
Track shopping cart state changes and count how many customers end up with
both product A and product B in their cart.

Operations:
- +a: add product A to cart
- -a: remove product A from cart  
- +b: add product B to cart
- -b: remove product B from cart

Goal: Count customers who have both A and B at the end of their session.

Algorithm: State Tracking with Counter Variables
Time Complexity: O(n×m) where n = customers, m = operations per customer
Space Complexity: O(1)

Submission Result: AC (23ms, 3.3MB)
Date: 2023-05-28 20:09
"""

def simulate_shopping_cart(operations, product_a_id, product_b_id):
    """
    Simulate shopping cart operations for a single customer
    
    Args:
        operations: list of integers representing cart operations
        product_a_id: ID of product A
        product_b_id: ID of product B
    
    Returns:
        bool: True if customer ends with both products A and B
    """
    # Track quantities of products A and B in cart
    product_a_count = 0
    product_b_count = 0
    
    # Process each operation
    for operation in operations:
        if operation == product_a_id:
            # Add product A
            product_a_count += 1
        elif operation == -product_a_id:
            # Remove product A (ensure non-negative)
            product_a_count -= 1
            if product_a_count < 0:
                product_a_count = 0
        elif operation == product_b_id:
            # Add product B
            product_b_count += 1
        elif operation == -product_b_id:
            # Remove product B (ensure non-negative)
            product_b_count -= 1
            if product_b_count < 0:
                product_b_count = 0
    
    # Customer has both products if both counts > 0
    return product_a_count >= 1 and product_b_count >= 1

def main():
    """
    Main execution function
    """
    # Read product IDs and number of customers
    product_a_id, product_b_id = map(int, input().split())
    num_customers = int(input())
    
    successful_customers = 0
    
    # Process each customer
    for i in range(num_customers):
        # Read operations for this customer
        operations = list(map(int, input().split()))
        
        # Simulate shopping cart for this customer
        has_both_products = simulate_shopping_cart(operations, product_a_id, product_b_id)
        
        if has_both_products:
            successful_customers += 1
    
    # Output the count of successful customers
    print(successful_customers)

if __name__ == "__main__":
    main()

"""
Algorithm Analysis:

1. Problem Model: E-commerce Cart Simulation
   - State tracking for individual shopping carts
   - Multiple customers with independent cart sessions
   - Binary success criterion (has both products)

2. State Management:
   - Two counters: product_a_count, product_b_count
   - Operations: increment/decrement based on add/remove
   - Non-negative constraint: can't have negative quantities

3. Operation Processing:
   - Positive value: add operation
   - Negative value: remove operation
   - Process sequentially to maintain state consistency

4. Success Condition:
   - Customer successful if final count A ≥ 1 AND final count B ≥ 1
   - Binary classification per customer
   - Aggregate count across all customers

5. Implementation Details:
   - Clear state variable naming
   - Bounds checking for non-negative quantities
   - Separate simulation logic from main control flow
   - Efficient single-pass processing per customer

6. Edge Cases Handled:
   - Remove operations when count is already 0
   - Multiple add/remove operations for same product
   - Customers with no operations
   - Operations involving only one product type

7. Real-world Application:
   - E-commerce analytics
   - Customer behavior tracking
   - Cart abandonment analysis
   - Product bundling effectiveness

Key Learning Points:
- State management in simulation problems
- Counter-based tracking systems
- Sequential operation processing
- Boolean condition evaluation
- E-commerce algorithm fundamentals
- Clean separation of simulation vs control logic
"""
