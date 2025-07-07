"""
ZeroJudge Problem d453: 三、最短距離 (Shortest Distance)
Problem Source: 98學年度板橋高中校內資訊學科能力競賽

Problem Description:
Find the shortest path between two points in a grid where '0' represents
walkable cells and '1' represents obstacles.

Algorithm: Breadth-First Search (BFS)
Time Complexity: O(n*m) where n and m are grid dimensions
Space Complexity: O(n*m) for visited set and queue

Submission Result: AC (18ms, 3.3MB)
Date: 2024-05-05 20:33
"""

def shortest_path(grid, start, end):
    """
    Find shortest path using BFS algorithm
    
    Args:
        grid: 2D list representing the maze ('0' = walkable, '1' = obstacle)
        start: tuple (x, y) starting position
        end: tuple (x, y) target position
    
    Returns:
        int: minimum steps to reach target, 0 if impossible
    """
    n = len(grid)      # Number of rows
    m = len(grid[0])   # Number of columns
    
    # BFS queue: (x, y, number_of_steps)
    queue = [(start[0], start[1], 1)]
    visited = set()    # Track visited cells to avoid cycles
    front = 0          # Manual queue pointer for efficiency
    
    while front < len(queue):
        x, y, steps = queue[front]
        front += 1
        
        # Check if we reached the target
        if (x, y) == end:
            return steps
        
        # Explore all 4 directions (up, down, left, right)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            
            # Check boundary conditions and walkability
            if (0 <= nx < n and 0 <= ny < m and 
                grid[nx][ny] == '0' and (nx, ny) not in visited):
                
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    
    return 0  # No path found

# Main execution
def main():
    N = int(input().strip())  # Number of test cases
    
    for i in range(N):
        # Read grid dimensions and coordinates
        n, m, x1, y1, x2, y2 = map(int, input().split())
        
        # Read the grid
        grid = [input().strip() for _ in range(n)]
        
        # Convert to 0-indexed coordinates
        start = (x1 - 1, y1 - 1)
        end = (x2 - 1, y2 - 1)
        
        # Find and print shortest path
        result = shortest_path(grid, start, end)
        print(result)

if __name__ == "__main__":
    main()

"""
Key Learning Points:
1. BFS guarantees shortest path in unweighted graphs
2. Using visited set prevents infinite loops
3. Manual queue pointer improves performance over deque.popleft()
4. Boundary checking prevents index errors
5. Converting to 0-indexed coordinates for easier array access
"""
