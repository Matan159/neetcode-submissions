class Solution:
    def isValid(self, s: str) -> bool:
        opening = set(['(', '{', '['])
        closing = set([')', '}', ']'])
        pairs = set([('(', ')'), ('{', '}'), ('[', ']')])
        stack = deque()
        for c in s:
            if c in opening:
                stack.append(c)
            elif c in closing:
                if len(stack) == 0:
                    return False
                opener = stack.pop()
                pair = (opener, c)
                if pair not in pairs:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        return False