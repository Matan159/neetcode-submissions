class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = [[] for _ in range(numCourses)]
        for preq in prerequisites:
            preqs[preq[0]].append(preq[1])
        
        def dfs(curr_course: int, preq_set: List[int]):
            if curr_course in preq_set:
                return False
            preq_set.append(curr_course)
            for i in preqs[curr_course]:
                if not dfs(i, preq_set):
                    return False
            preq_set.pop()
            return True

        for preq in preqs:
            for p in preq:
                if not dfs(p, []):
                    return False

        return True