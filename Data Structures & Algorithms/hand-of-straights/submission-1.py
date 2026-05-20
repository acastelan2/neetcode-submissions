class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counts = Counter(hand)
        hand.sort()

        for card in hand:
            if counts[card] > 0:
                counts[card] -= 1
                
                for i in range(1, groupSize):
                    if counts[card+i] > 0:
                        counts[card+i] -= 1
                    else:
                        return False
        return True
        