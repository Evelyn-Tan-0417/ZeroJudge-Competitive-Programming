"""
ZeroJudge Problem c294: APCS-2016-1029-1三角形辨別 (Triangle Classification)
Problem Source: 2016年10月APCS

Problem Description:
Given three side lengths, determine:
1. Whether they can form a valid triangle
2. If valid, classify as: Acute, Right, or Obtuse

Triangle validity: sum of any two sides > third side
Triangle classification (using Pythagorean theorem):
- a² + b² < c²  → Obtuse
- a² + b² = c²  → Right  
- a² + b² > c²  → Acute
(where c is the longest side)

Algorithm: Geometric Analysis with Mathematical Classification
Time Complexity: O(1)
Space Complexity: O(1)

Submission Result: AC (16ms, 3.4MB)
Date: 2022-07-29 10:38
"""

def classify_triangle(side1, side2, side3):
    """
    Classify triangle based on side lengths
    
    Args:
        side1, side2, side3: triangle side lengths
    
    Returns:
        tuple: (sides_sorted, is_valid, classification)
               sides_sorted: sorted sides [a, b, c] where c is longest
               is_valid: boolean indicating if triangle is valid
               classification: "Acute", "Right", "Obtuse", or None
    """
    # Sort sides to ensure c is the longest side
    sides = sorted([side1, side2, side3])
    a, b, c = sides[0], sides[1], sides[2]
    
    # Check triangle inequality: sum of any two sides > third side
    # Since sides are sorted, we only need to check if a + b > c
    is_valid = (a + b > c)
    
    if not is_valid:
        return sides, False, None
    
    # Classify triangle using Pythagorean theorem
    # Compare a² + b² with c²
    sum_of_squares = a * a + b * b
    longest_square = c * c
    
    if sum_of_squares < longest_square:
        classification = "Obtuse"
    elif sum_of_squares == longest_square:
        classification = "Right"
    else:  # sum_of_squares > longest_square
        classification = "Acute"
    
    return sides, True, classification

def main():
    """
    Main execution function
    """
    # Read three side lengths
    sides_input = list(map(int, input().split()))
    side1, side2, side3 = sides_input[0], sides_input[1], sides_input[2]
    
    # Classify the triangle
    sorted_sides, is_valid, classification = classify_triangle(side1, side2, side3)
    
    # Output results
    print(sorted_sides[0], sorted_sides[1], sorted_sides[2])
    
    if not is_valid:
        print("No")
    else:
        print(classification)

if __name__ == "__main__":
    main()

"""
Algorithm Analysis:

1. Geometric Theory Applied:
   - Triangle Inequality Theorem: sum of any two sides > third side
   - Pythagorean Theorem: relationship between sides and angles
   - Law of Cosines: generalization for angle classification

2. Triangle Validity Check:
   - Must satisfy: a + b > c, a + c > b, b + c > a
   - Optimization: sort sides, only check a + b > c (sufficient)
   - Mathematical proof: if a ≤ b ≤ c, other inequalities follow

3. Triangle Classification Logic:
   - Based on relationship between a² + b² and c²
   - Obtuse: largest angle > 90° ⟺ a² + b² < c²
   - Right: largest angle = 90° ⟺ a² + b² = c²
   - Acute: largest angle < 90° ⟺ a² + b² > c²

4. Implementation Strategy:
   - Sort sides to identify longest side (c)
   - Use integer arithmetic to avoid floating-point precision issues
   - Clear conditional logic for classification

5. Mathematical Insight:
   - Largest angle is always opposite the longest side
   - Pythagorean theorem determines angle type
   - Integer comparisons more reliable than angle calculations

6. Edge Cases:
   - Degenerate triangles (zero area): a + b = c
   - Equilateral triangles: a = b = c
   - Isosceles triangles: two equal sides
   - Scalene triangles: all sides different

7. Geometric Applications:
   - Computer graphics and CAD systems
   - Surveying and navigation
   - Engineering design validation
   - Educational geometry tools

Key Learning Points:
- Triangle inequality theorem application
- Pythagorean theorem for angle classification
- Sorting for mathematical optimization
- Integer arithmetic in geometric calculations
- Conditional logic for mathematical classification
- Fundamental computational geometry concepts
"""
