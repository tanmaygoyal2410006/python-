"""
GGiven a lowercase string array arr[]. Each element in the array represents a vote cast 
for a candidate. Return the name of the candidate who received the maximum number 
of votes and the count of votes he received. In case of a tie between two or more 
candidates, return the lexicographically smallest name.
Note: Return an array of strings, the winning candidate name as the first element and 
the vote count as the second element (typecast the count to string).
Examples :
Input: arr[] = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", 
"john", "johnny", "jamie", "johnny", "john"]
Output: ["john", "4"]
Explanation: "john" has 4 votes casted for him, but so does "johnny". "john" is 
lexicographically smaller, so we print "john" and the votes he received.
Input: n = 3
arr[] = ["andy", "blake", "clark"]
Output: ["Andy", "1"]
Explanation: All the candidates get 1 votes each. We print "andy" as it is 
lexicographically smaller"
"""
from collections import Counter

def winner(arr):
    freq = Counter(arr)
    max_votes = max(freq.values())
    
    candidates = [k for k in freq if freq[k] == max_votes]
    
    name = min(candidates)
    
    return [name, str(max_votes)]
