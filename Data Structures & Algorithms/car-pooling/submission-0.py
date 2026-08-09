class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = [0]*1001
        curr_peeps = 0

        for i in range(len(trips)):
            changes[trips[i][1]]+=trips[i][0]
            changes[trips[i][2]]-=trips[i][0]
        
        for j in changes:
            curr_peeps+=j
            if curr_peeps>capacity:
                return False
            
        return True