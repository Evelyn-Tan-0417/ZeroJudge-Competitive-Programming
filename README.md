# Competitive Programming Portfolio - ZeroJudge Platform

![ZeroJudge](https://img.shields.io/badge/Platform-ZeroJudge-blue)
![Language](https://img.shields.io/badge/Language-Python-green)
![Success Rate](https://img.shields.io/badge/Success%20Rate-100%25-brightgreen)
![Problems Solved](https://img.shields.io/badge/Problems%20Solved-13-orange)

## Achievement Summary

- **Platform:** [ZeroJudge.tw](https://zerojudge.tw/) - Taiwan's premier programming education platform
- **Problems Solved:** 13/13 (100% success rate)
- **Time Period:** July 2022 - May 2024 (2 years)
- **Language:** Python
- **Problem Sources:** APCS competitions, UVa Online Judge, educational challenges

## About ZeroJudge Platform

ZeroJudge is Taiwan's largest educational programming platform with over **4 million evaluated submissions**. Unlike competition-focused platforms, ZeroJudge emphasizes learning with detailed Chinese error messages and comprehensive educational support, making it ideal for structured competitive programming education.

## Technical Skills Demonstrated

### Algorithms & Data Structures

- **Graph Algorithms:** BFS shortest path traversal with queue management
- **Optimization:** Greedy algorithms with binary search optimization
- **Mathematical Computing:** Number theory, sequence analysis, and cycle detection
- **String Processing:** Pattern matching, text manipulation, and parsing
- **Array Operations:** Statistical analysis, data processing, and state tracking

### Programming Concepts

- Complex data structure manipulation (2D arrays, queues, sets)
- Algorithm optimization techniques (binary search, greedy approaches)
- Efficient input/output handling for competitive programming
- Mathematical computation and validation
- Boolean logic and conditional processing

## Repository Structure

```
📦 ZeroJudge-Competitive-Programming
├── 📂 src/
│   ├── 📂 graph-algorithms/
│   │   └── d453_shortest_path.py
│   ├── 📂 optimization/
│   │   ├── j608_machine_rental.py
│   │   ├── f312_resource_allocation.py
│   │   ├── f605_purchasing_power.py
│   │   └── g595_fence_repair.py
│   ├── 📂 number-theory/
│   │   └── d442_happy_numbers.py
│   ├── 📂 string-processing/
│   │   ├── g275_couplet_analysis.py
│   │   └── c290_secret_difference.py
│   ├── 📂 array-manipulation/
│   │   ├── e286_basketball_game.py
│   │   ├── f579_shopping_cart.py
│   │   └── c461_logic_operators.py
│   └── 📂 geometry/
│       └── c294_triangle_classification.py
├── 📂 docs/
│   ├── problem-summaries.md
└── 📂 assets/
    └── zerojudge submission.jpg/
```

## Problem Categories & Solutions

### Graph Algorithms (1 problem)

| Problem ID | Title | Difficulty | Key Concepts |
|------------|-------|------------|--------------|
| d453 | 三、最短距離 (Shortest Distance) | ⭐⭐⭐ | BFS, Grid Traversal, Queue Management |

### Optimization Problems (4 problems)

| Problem ID | Title | Difficulty | Key Concepts |
|------------|-------|------------|--------------|
| j608 | 4. 機器出租 (Machine Rental) | ⭐⭐⭐⭐ | Greedy Algorithm, Binary Search |
| f312 | 1. 人力分配 (Resource Allocation) | ⭐⭐⭐ | Quadratic Optimization |
| f605 | 1. 購買力 (Purchasing Power) | ⭐⭐ | Conditional Logic, Statistics |
| g595 | 1. 修補圍籬 (Fence Repair) | ⭐⭐ | Array Processing, Minimum Cost |

### Mathematical Computing (1 problem)

| Problem ID | Title | Difficulty | Key Concepts |
|------------|-------|------------|--------------|
| d442 | 10591 - Happy Number | ⭐⭐⭐ | Number Theory, Cycle Detection |

### String Processing (2 problems)

| Problem ID | Title | Difficulty | Key Concepts |
|------------|-------|------------|--------------|
| g275 | 1. 七言對聯 (Couplet Analysis) | ⭐⭐⭐ | Pattern Matching, String Analysis |
| c290 | APCS 2017-0304-1秘密差 (Secret Difference) | ⭐⭐ | String Manipulation, Mathematical Logic |

### Array Manipulation (3 problems)

| Problem ID | Title | Difficulty | Key Concepts |
|------------|-------|------------|--------------|
| e286 | 籃球比賽 (Basketball Game) | ⭐⭐ | Statistical Analysis, Conditional Logic |
| f579 | 1. 購物車 (Shopping Cart) | ⭐⭐ | State Tracking, Counting |
| c461 | APCS 邏輯運算子 (Logic Operators) | ⭐⭐ | Boolean Algebra, Logic Gates |

### Geometry (1 problem)

| Problem ID | Title | Difficulty | Key Concepts |
|------------|-------|------------|--------------|
| c294 | APCS-2016-1029-1三角形辨別 (Triangle Classification) | ⭐⭐ | Geometric Analysis, Mathematical Classification |

## Learning Progression Timeline

**Phase 1: Foundation Building (Jul - Oct 2022)**

- Started with basic logic and geometric problems
- Mastered fundamental input/output and conditional logic
- Problems: `c294`, `c290`, `c461`

**Phase 2: Advanced Problem Solving (May 2023)**

- Tackled complex optimization and array manipulation
- Developed statistical analysis and state tracking skills
- Problems: `g595`, `f605`, `f312`, `f579`, `e286`, `g275`

**Phase 3: Algorithm Mastery (Aug 2023 - May 2024)**

- Implemented sophisticated algorithms including graph traversal
- Advanced optimization with binary search and mathematical computing
- Problems: `d442`, `j608`, `d453`

## Highlighted Solutions

### Most Complex: d453 - Shortest Path (BFS Implementation)

```python
def shortest_path(grid, start, end):
    n, m = len(grid), len(grid[0])
    queue = [(start[0], start[1], 1)]  # (x, y, steps)
    visited = set()
    front = 0
    
    while front < len(queue):
        x, y, steps = queue[front]
        front += 1
        
        if (x, y) == end:
            return steps
            
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n and 0 <= ny < m and 
                grid[nx][ny] == '0' and (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    
    return 0
```

## Educational Impact

This portfolio represents **structured learning under tutor guidance**, emphasizing:

- Progressive skill development from basic to advanced algorithms
- Systematic approach to problem categorization and solution strategies
- Deep understanding of fundamental computer science concepts
- Strong foundation for advanced programming and data structures

## Platform Performance

All submissions achieved **"AC" (Accepted)** status with competitive performance metrics:

- **Runtime:** Consistently within time limits (16ms - 2.9s)
- **Memory Usage:** Efficient memory management (3.3MB - 32.1MB)
- **Success Rate:** 100% first-time acceptance rate

## Additional Documentation

- [Problem Summaries](docs/problem_summaries.md) - Detailed analysis of each challenge
- [Submission Screenshots](assets/zerojudge-submission.jpg/) - Platform evidence and achievements

---

**About the Author:** This portfolio represents 2 years of dedicated competitive programming practice, demonstrating consistent technical growth and strong problem-solving foundations essential for computer science education and software development careers.

**Last Updated:** January 2025
