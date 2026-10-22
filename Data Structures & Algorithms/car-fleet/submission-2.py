class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # gather fleets and sort them by starting position O(NlogN)
        fleets = list(zip(position, speed)) # [(position, speed), ...]
        fleets.sort(key= lambda x: x[0], reverse=True) # 

        # for all fleets, check if the current fleet catches the fleet ahead of it
        # Catches -> merge fleets with high position and slow speed and push to stack
        # Doesnt catch -> push farther fleet and the push closer fleet
        res = deque()
        for fleet in fleets:
            if len(res) == 0:
                res.append(fleet)
                continue
            front_fleet_time = (target-res[-1][0])/res[-1][1] # time = (target_dist-start_pos) / speed
            back_fleet_time = (target-fleet[0])/fleet[1]
            if back_fleet_time > front_fleet_time: # if back doesnt catch the front, keep both
                res.append(fleet)

        return len(res) # return amount of fleets not merged
