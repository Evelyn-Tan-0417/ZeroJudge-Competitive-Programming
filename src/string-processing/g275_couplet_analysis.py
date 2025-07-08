"""
ZeroJudge Problem g275: 1. 七言對聯 (Couplet Analysis)
Problem Source: 2021年9月APCS

Problem Description:
Analyze traditional Chinese seven-character couplets for three types of violations:
A. Rhythm violation: positions 2,4,6 should follow specific patterns
B. Tone violation: first line should end with flat tone (0), second with rising tone (1)
C. Character repetition: same characters shouldn't appear in corresponding positions

Format: Each line has 7 elements: char1 tone1 char2 tone2 char3 tone3 final_tone

Algorithm: Pattern Matching with Complex Rule Validation
Time Complexity: O(1) per couplet (fixed number of checks)
Space Complexity: O(1)

Submission Result: AC (20ms, 3.3MB)
Date: 2023-05-28 20:37
"""

def analyze_couplet_violations(line1, line2):
    """
    Analyze a couplet for rhythm, tone, and character violations
    
    Args:
        line1: list of 7 elements [char1, tone1, char2, tone2, char3, tone3, final_tone]
        line2: list of 7 elements [char1, tone1, char2, tone2, char3, tone3, final_tone]
    
    Returns:
        str: violation codes concatenated (e.g., "ABC", "A", "BC", or empty string)
    """
    violations = ""
    
    # Check Violation A: Rhythm patterns
    # Positions 2, 4, 6 (indices 1, 3, 5 in tone positions)
    # Rule: tones at positions 2&4 should be same, and different from position 6
    # OR: tones at positions 2&6 should be same, and different from position 4
    
    # Extract tones at positions 2, 4, 6 for both lines
    line1_tone2, line1_tone4, line1_tone6 = line1[1], line1[3], line1[5]
    line2_tone2, line2_tone4, line2_tone6 = line2[1], line2[3], line2[5]
    
    # Check rhythm violations for line 1
    line1_rhythm_ok = (line1_tone2 == line1_tone4 and line1_tone2 != line1_tone6) or \
                      (line1_tone2 == line1_tone6 and line1_tone2 != line1_tone4)
    
    # Check rhythm violations for line 2  
    line2_rhythm_ok = (line2_tone2 == line2_tone4 and line2_tone2 != line2_tone6) or \
                      (line2_tone2 == line2_tone6 and line2_tone2 != line2_tone4)
    
    if not line1_rhythm_ok or not line2_rhythm_ok:
        violations += "A"
    
    # Check Violation B: Final tone pattern
    # First line should end with flat tone (0), second line with rising tone (1)
    line1_final_tone = line1[6]  # Last element
    line2_final_tone = line2[6]  # Last element
    
    if line1_final_tone != '0' or line2_final_tone != '1':
        violations += "B"
    
    # Check Violation C: Character repetition in corresponding positions
    # Characters at positions 1, 3, 5 (indices 0, 2, 4) shouldn't repeat
    line1_chars = [line1[0], line1[2], line1[4]]  # Characters at positions 1, 3, 5
    line2_chars = [line2[0], line2[2], line2[4]]  # Characters at positions 1, 3, 5
    
    character_repetition = False
    for i in range(3):
        if line1_chars[i] == line2_chars[i]:
            character_repetition = True
            break
    
    if character_repetition:
        violations += "C"
    
    return violations

def main():
    """
    Main execution function
    """
    n = int(input())  # Number of couplets
    results = []
    
    for i in range(n):
        # Read first line of couplet
        line1 = input().split()
        
        # Read second line of couplet
        line2 = input().split()
        
        # Analyze violations
        violations = analyze_couplet_violations(line1, line2)
        
        # Store result (None for no violations, violation string otherwise)
        if violations == "":
            results.append(None)
        else:
            results.append(violations)
    
    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

"""
Algorithm Analysis:

1. Problem Domain: Traditional Chinese Poetry Analysis
   - Seven-character couplets with specific rules
   - Multiple validation criteria with different priorities
   - Cultural algorithm application

2. Rule System Implementation:
   A. Rhythm Analysis:
      - Extract tones at specific positions (2, 4, 6)
      - Check for valid rhythm patterns
      - Apply to both lines independently
   
   B. Tone Pattern Validation:
      - Simple final tone checking
      - Line 1: flat tone (0), Line 2: rising tone (1)
   
   C. Character Repetition Detection:
      - Position-wise character comparison
      - Check positions 1, 3, 5 between lines

3. Data Structure:
   - Input: List of 7 elements per line
   - Positions: [char, tone, char, tone, char, tone, final_tone]
   - Access: Direct indexing for specific positions

4. Validation Logic:
   - Independent rule checking
   - String concatenation for multiple violations
   - Early termination for character repetition check

5. Cultural Context:
   - Traditional Chinese prosody rules
   - Tonal patterns in classical poetry
   - Character balance and variation requirements

Key Learning Points:
- Complex rule system implementation
- String parsing and element extraction
- Multi-criteria validation logic
- Cultural algorithm applications
- Pattern matching in structured text
"""
