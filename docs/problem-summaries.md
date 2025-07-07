Problem Summaries & Technical Analysis
Overview
This document provides detailed analysis of all 13 ZeroJudge problems solved, including algorithmic approaches, complexity analysis, and key learning outcomes.

🌐 Graph Algorithms
d453: 三、最短距離 (Shortest Distance)
Source: 98學年度板橋高中校內資訊學科能力競賽

Difficulty: ⭐⭐⭐

Submission: AC (18ms, 3.3MB) - 2024-05-05

Problem Description:

Find the shortest path between two points in a grid maze where '0' represents walkable paths and '1' represents obstacles.

Algorithm Used: Breadth-First Search (BFS)

Key Concepts: Graph traversal, shortest path, queue management

Time Complexity: O(n×m)

Space Complexity: O(n×m)

Technical Highlights:

Implemented proper BFS with visited set to prevent cycles
Used manual queue pointer for performance optimization
Handled coordinate conversion from 1-indexed to 0-indexed
Demonstrated understanding of graph theory fundamentals
⚡ Optimization Problems
j608: 4. 機器出租 (Machine Rental)
Source: 2023年1月APCS

Difficulty: ⭐⭐⭐⭐

Submission: AC (0.4s, 32.1MB) - 2024-03-31

Problem Description:

Given n rental requests with start/end times and k machines, maximize the number of fulfilled requests.

Algorithm Used: Greedy Algorithm with Binary Search

Key Concepts: Interval scheduling, greedy optimization, binary search

Time Complexity: O(n log n + n log k)

Space Complexity: O(n + k)

Technical Highlights:

Applied greedy choice: process by earliest end time
Used bisect module for O(log k) machine selection
Demonstrated understanding of optimal substructure
Advanced optimization technique for competitive programming
f312: 1. 人力分配 (Resource Allocation)
Source: 2020年10月APCS

Difficulty: ⭐⭐⭐

Submission: AC (18ms, 3.3MB) - 2023-05-28

Problem Description:

Optimize allocation of n people between two projects with quadratic productivity functions.

Algorithm Used: Exhaustive Search with Mathematical Optimization

Key Concepts: Quadratic functions, optimization, mathematical modeling

Time Complexity: O(n)

Space Complexity: O(1)

Technical Highlights:

Evaluated all possible allocations efficiently
Applied quadratic function analysis
Demonstrated mathematical problem-solving skills
f605: 1. 購買力 (Purchasing Power)
Source: 2021年1月APCS

Difficulty: ⭐⭐

Submission: AC (22ms, 3.3MB) - 2023-05-28

Problem Description:

Calculate total purchasing power and valid stores based on price difference thresholds.

Algorithm Used: Statistical Analysis with Conditional Logic

Key Concepts: Array processing, statistical analysis, conditional counting

Time Complexity: O(n×m)

Space Complexity: O(1)

Technical Highlights:

Processed multi-dimensional data efficiently
Applied statistical measures (min, max, sum)
Demonstrated data analysis fundamentals
g595: 1. 修補圍籬 (Fence Repair)
Source: 2021年11月APCS

Difficulty: ⭐⭐

Submission: AC (18ms, 3.3MB) - 2023-05-28

Problem Description:

Calculate minimum cost to repair fence segments based on neighboring values.

Algorithm Used: Array Processing with Boundary Handling

Key Concepts: Array manipulation, edge case handling, optimization

Time Complexity: O(n)

Space Complexity: O(1)

Technical Highlights:

Handled boundary conditions for first/last elements
Applied minimum value selection for optimization
Demonstrated careful edge case analysis
🔢 Mathematical Computing
d442: 10591 - Happy Number
Source: UVa10591

Difficulty: ⭐⭐⭐

Submission: AC (2.9s, 3.3MB) - 2023-08-06

Problem Description:

Determine if a number is "happy" (eventually reaches 1) or "unhappy" (enters a cycle) when repeatedly replacing it with the sum of squares of its digits.

Algorithm Used: Cycle Detection with Set Tracking

Key Concepts: Number theory, cycle detection, mathematical sequences

Time Complexity: O(k) where k is cycle length

Space Complexity: O(k)

Technical Highlights:

Implemented cycle detection using set membership
Applied mathematical transformation (sum of digit squares)
Demonstrated understanding of sequence analysis
Handled multiple test cases with proper formatting
📝 String Processing
g275: 1. 七言對聯 (Couplet Analysis)
Source: 2021年9月APCS

Difficulty: ⭐⭐⭐

Submission: AC (20ms, 3.3MB) - 2023-05-28

Problem Description:

Analyze traditional Chinese couplets for pattern violations in rhythm, tone, and character usage.

Algorithm Used: Pattern Matching with Complex Rule Validation

Key Concepts: String analysis, pattern matching, logical rule systems

Time Complexity: O(1) per couplet

Space Complexity: O(1)

Technical Highlights:

Implemented complex rule validation system
Applied string indexing and comparison
Demonstrated cultural algorithm application
Handled multiple validation criteria simultaneously
c290: APCS 2017-0304-1秘密差 (Secret Difference)
Source: 2017年3月APCS

Difficulty: ⭐⭐

Submission: AC (16ms, 3.3MB) - 2022-07-29

Problem Description:

Calculate the absolute difference between sums of digits at even and odd positions.

Algorithm Used: String Indexing with Mathematical Calculation

Key Concepts: String manipulation, indexing, mathematical operations

Time Complexity: O(n) where n is string length

Space Complexity: O(n)

Technical Highlights:

Applied modular arithmetic for position determination
Used list comprehension for efficient processing
Demonstrated string-to-number conversion skills
📊 Array Manipulation
e286: 籃球比賽 (Basketball Game)
Source: APCS

Difficulty: ⭐⭐

Submission: AC (18ms, 3.4MB) - 2023-05-28

Problem Description:

Determine game outcome based on scores from two basketball games.

Algorithm Used: Statistical Analysis with Conditional Logic

Key Concepts: Array summation, statistical comparison, game logic

Time Complexity: O(n)

Space Complexity: O(1)

Technical Highlights:

Applied statistical aggregation (sum function)
Implemented multi-stage conditional logic
Demonstrated sports analytics programming
f579: 1. 購物車 (Shopping Cart)
Source: 2020年7月APCS

Difficulty: ⭐⭐

Submission: AC (23ms, 3.3MB) - 2023-05-28

Problem Description:

Track shopping cart state changes and count valid combinations.

Algorithm Used: State Tracking with Counter Variables

Key Concepts: State management, counting algorithms, array processing

Time Complexity: O(n×m)

Space Complexity: O(1)

Technical Highlights:

Implemented stateful counting system
Applied increment/decrement logic for cart tracking
Demonstrated e-commerce algorithm fundamentals
c461: APCS 邏輯運算子 (Logic Operators)
Source: APCS

Difficulty: ⭐⭐

Submission: AC (16ms, 3.3MB) - 2022-07-30

Problem Description:

Determine which logical operators (AND, OR, XOR) produce the correct output for given inputs.

Algorithm Used: Boolean Logic Evaluation

Key Concepts: Boolean algebra, logic gates, truth tables

Time Complexity: O(1)

Space Complexity: O(1)

Technical Highlights:

Applied fundamental Boolean operations
Implemented truth table validation
Demonstrated digital logic understanding
Used list accumulation for multiple valid answers
📐 Geometry
c294: APCS-2016-1029-1三角形辨別 (Triangle Classification)
Source: 2016年10月APCS

Difficulty: ⭐⭐

Submission: AC (16ms, 3.4MB) - 2022-07-29

Problem Description:

Classify triangles as valid/invalid and determine if they are acute, right, or obtuse.

Algorithm Used: Geometric Analysis with Mathematical Classification

Key Concepts: Geometry, triangle inequality, Pythagorean theorem

Time Complexity: O(1)

Space Complexity: O(1)

Technical Highlights:

Applied triangle inequality theorem for validity
Used Pythagorean theorem for angle classification
Implemented mathematical comparison logic
Demonstrated geometric algorithm fundamentals
📈 Learning Progression Analysis
Technical Growth Indicators:
Complexity Evolution:

2022: Basic logic and geometry (⭐⭐ difficulty)
2023: Advanced optimization and data structures (⭐⭐⭐ difficulty)
2024: Graph algorithms and complex optimization (⭐⭐⭐⭐ difficulty)
Algorithm Sophistication:

Early: Simple conditionals and basic math
Middle: Array processing and statistical analysis
Advanced: Graph traversal, binary search optimization, cycle detection
Code Quality Improvements:

Readability: Progressed from basic variable names to descriptive identifiers
Efficiency: Advanced from brute force to optimized algorithms
Structure: Evolved from linear scripts to modular, well-documented solutions
Problem-Solving Maturity:

Pattern Recognition: Ability to identify optimal algorithm types
Optimization Awareness: Conscious consideration of time/space complexity
Edge Case Handling: Comprehensive boundary condition management
This progression demonstrates systematic skill development and strong foundation for advanced computer science coursework.

