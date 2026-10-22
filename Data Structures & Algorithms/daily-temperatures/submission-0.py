class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = deque() # [(temp, index),...]
        for i, temp in enumerate(temperatures): # traverse the temperature list
            # if this loops runs, a temperature rise has been found
            while len(stack) > 0 and temp > stack[-1][0]: # pop from stack and fill in result as long as there are colder days in the stack
                pair = stack.pop()
                result[pair[1]] = i - pair[1]
            stack.append((temp, i)) # temp is decreasing, push to the stack
        return result
