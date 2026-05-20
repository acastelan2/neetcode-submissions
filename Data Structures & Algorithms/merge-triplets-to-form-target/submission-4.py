class Solution:
    def mergeTriplets(self, triplets, target) -> bool:
        if len(triplets) == 1:
            return triplets[0] == target
        
        x,y,z = ([False, False] for _ in range(3)) # [mergeable, seen]
        
        for a,b,c in triplets:
            if a == target[0]:
                x[1] = True
                y[0] = b <= target[1]
                z[0] = c <= target[2]
            if b == target[1]:
                y[1] = True
                x[0] = a <= target[0]
                z[0] = c <= target[2]  
            if c == target[2]:
                z[1] = True
                x[0] = a <= target[0]
                y[0] = b <= target[1] 

            if all(x) and all(y) and all(z):
                return True

        return False