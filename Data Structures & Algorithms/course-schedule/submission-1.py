class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make a dictionary 
        # do bfs for each course to see if there is a cycle
        dictionary = {i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            dictionary[crs].append(pre)

        path = set()
        def dfs(course):
            if course in path:
                return False
            if dictionary[course] == []:
                return True

            path.add(course)
            for prerex in dictionary[course]:
                if not dfs(prerex):
                    return False
            path.remove(course)
            dictionary[course] = []
            return True            


        for course in dictionary:
            if not dfs(course):
                return False

        return True


            