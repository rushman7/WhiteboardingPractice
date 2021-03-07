class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if len(piles) == 2:
            return True
        
        left, right, player1, player2 = 0,len(piles)-1,0,0
        curr_turn = True
        
        while left <= right:
            if piles[left] >= piles[right]:
                if curr_turn: player1 += piles[left]
                else: player2 += piles[left]
                left+=1
            else:
                if curr_turn: player1 += piles[right]
                else: player2 += piles[right]
                right-=1
            curr_turn = not curr_turn
        
        return player1 if player1 > player2 else player2
