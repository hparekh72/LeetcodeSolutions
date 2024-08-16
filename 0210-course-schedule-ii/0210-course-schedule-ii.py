# Topological Sort
# TC: O(V + E) + (V) (reverse), V = number of courses
# SC: O(V)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Create an adjacency list
        pre = defaultdict(list)
        for course, prerequisite in prerequisites:
            pre[course].append(prerequisite)

        # Topological Sort

        queue = deque()
        indegree = [0] * numCourses

        for node in pre:
            for neighbor in pre[node]:
                indegree[neighbor] += 1

        # Add the nodes in the queue whose indegree is 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            node = queue.popleft()
            res.append(node)

            for neighbor in pre[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(res) == numCourses:
            self.reverse(res)
            return res
        else:
            return []

    def reverse(self, res):
        i, j = 0, len(res) - 1
        while i < j:
            print(res[i], res[j])
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        
            