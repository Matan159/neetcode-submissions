class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque() # [(index, height), ...]
        max_area = 0
        for i, h in enumerate(heights): # enumerate the input
            # as long as height is increasing, push to stack with current height
            if len(stack) == 0 or h > stack[-1][1]:
                stack.append((i,h))
            # if hieght not increasing, run while loop until stack is in increasing height
            else:
                left_edge = 0
                while len(stack)>0 and h <= stack[-1][1]:
                    # every pop update max_area and check how much further to the left the bar can extend, insert to index
                    index, height = stack.pop()
                    max_area = max(max_area, (i-index)*height)
                    left_edge = index
                stack.append((left_edge, h))
                
        # only the ascending stack remains
        # for every remaining pair, update max_area
        l = len(heights)
        for i, h in stack:
            max_area = max(max_area, (l-i)*h)
        return max_area