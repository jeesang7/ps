class Solution:
    def numberOfMatches(self, n: int) -> int:
        game_on = True
        matches = 0
        teams = n
        while game_on:
            matches += int(teams/2)
            if teams % 2 == 1:
                teams = int(teams/2) + 1
            else:
                teams = int(teams/2)
            
            print(matches, teams)
            
            if floor(teams) == 1:
                break
        
        return matches
