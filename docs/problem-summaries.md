# Problem Summaries & Technical Analysis

## Overview

This document provides detailed analysis of all 13 ZeroJudge problems solved, including algorithmic approaches, complexity analysis, and key learning outcomes.

---

## 🌐 Graph Algorithms

### d453: 三、最短距離 (Shortest Distance)

**Source:** 98學年度板橋高中校內資訊學科能力競賽

**Difficulty:** ⭐⭐⭐

**Submission:** AC (18ms, 3.3MB) - 2024-05-05

**Problem Description:**

Find the shortest path between two points in a grid maze where '0' represents walkable paths and '1' represents obstacles.

**Algorithm Used:** Breadth-First Search (BFS)

**Key Concepts:** Graph traversal, shortest path, queue management

**Time Complexity:** O(n×m)

**Space Complexity:** O(n×m)

**Technical Highlights:**

- Implemented proper BFS with visited set to prevent cycles
- Used manual queue pointer for performance optimization  
- Handled coordinate conversion from 1-indexed to 0-indexed
- Demonstrated understanding of graph theory fundamentals
