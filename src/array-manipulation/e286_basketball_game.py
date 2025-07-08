"""
ZeroJudge Problem e286: 籃球比賽 (Basketball Game)
Problem Source: APCS

Problem Description:
Determine the outcome of a basketball tournament based on scores from two games.
Rules:
- Win a game if your total score > opponent's total score
- Tournament result: Win (2 games won), Tie (1 game won), Lose (0 games won)

Input: 4 lines of scores
- Line 1: Our team's scores in game 1
- Line 2: Opponent's scores in game 1  
- Line 3: Our team's scores in game 2
- Line 4: Opponent's scores in game 2

Algorithm: Statistical Analysis with Conditional Logic
Time Complexity: O(n) where n is number of scores per game
Space Complexity: O(1)

Submission Result: AC (18ms, 3.4MB)
Date: 2023-05-28 20:15
"""

def determine_tournament_result(our_scores_game1, opponent_scores_game1, 
                               our_scores_game2, opponent_scores_game2):
    """
    Determine tournament result based on two basketball games
    
    Args:
        our_scores_game1: list of our team's scores in game 1
        opponent_scores_game1: list of opponent's scores in game 1
        our_scores_game2: list of our team's scores in game 2
        opponent_scores_game2: list of opponent's scores in game 2
    
    Returns:
        tuple: (games_won, game1_result, game2_result, tournament_result)
    """
    # Calculate total scores for game 1
    our_total_game1 = sum(our_scores_game1)
    opponent_total_game1 = sum(opponent_scores_game1)
    
    # Calculate total scores for game 2
    our_total_game2 = sum(our_scores_game2)
    opponent_total_game2 = sum(opponent_scores_game2)
    
    # Determine game results and count wins
    games_won = 0
    
    # Game 1 result
    game1_result = f"{our_total_game1}:{opponent_total_game1}"
    if our_total_game1 > opponent_total_game1:
        games_won += 1
    
    # Game 2 result
    game2_result = f"{our_total_game2}:{opponent_total_game2}"
    if our_total_game2 > opponent_total_game2:
        games_won += 1
    
    # Determine tournament result
    if games_won == 2:
        tournament_result = "Win"
    elif games_won == 1:
        tournament_result = "Tie"
    else:  # games_won == 0
        tournament_result = "Lose"
    
    return games_won, game1_result, game2_result, tournament_result

def main():
    """
    Main execution function
    """
    # Read scores for all games
    our_scores_game1 = list(map(int, input().split()))
    opponent_scores_game1 = list(map(int, input().split()))
    our_scores_game2 = list(map(int, input().split()))
    opponent_scores_game2 = list(map(int, input().split()))
    
    # Determine tournament result
    games_won, game1_result, game2_result, tournament_result = determine_tournament_result(
        our_scores_game1, opponent_scores_game1, our_scores_game2, opponent_scores_game2
    )
    
    # Output results
    print(game1_result)
    print(game2_result)
    print(tournament_result)

if __name__ == "__main__":
    main()

"""
Algorithm Analysis:

1. Problem Structure:
   - Two-game tournament with aggregate scoring
   - Individual game winner determined by total score
   - Tournament winner determined by games won (2/1/0)

2. Statistical Operations:
   - sum() function for score aggregation
   - Comparison operations for winner determination
   - Counting wins across multiple games

3. Game Logic Implementation:
   - Binary outcome per game (win/lose, no ties mentioned)
   - Tournament scoring: 2 wins = Win, 1 win = Tie, 0 wins = Lose
   - Clear mapping from individual games to tournament result

4. Data Processing Flow:
   - Input: 4 arrays of scores
   - Processing: 2 aggregations + 2 comparisons
   - Output: 2 game results + 1 tournament result

5. Implementation Details:
   - Use sum() for efficient array aggregation
   - String formatting for score display (total1:total2)
   - Counter variable for tracking wins
   - Conditional logic for tournament outcome

6. Output Format:
   - Game results: "our_total:opponent_total"
   - Tournament result: "Win"/"Tie"/"Lose"
   - Clear, readable output format

Key Learning Points:
- Statistical aggregation of arrays
- Multi-stage conditional logic
- Game/tournament result determination
- String formatting for score display
- Clear separation of game vs tournament logic
- Sports analytics programming fundamentals
"""
