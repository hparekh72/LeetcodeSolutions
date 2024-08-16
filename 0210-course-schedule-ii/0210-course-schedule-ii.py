# Topological Sort
# TC: O(V + E), V = number of courses, E = number of edges(prerequisites)
# SC: O(V + E) (adjacency list & indegree) + O(V) (queue & result) ~ O(V)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Create an adjacency list # TC: O(E)
        pre = defaultdict(list) 
        for course, prerequisite in prerequisites:
            pre[prerequisite].append(course)        

        # Calculate the indegree for each node # TC: O(E)
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            indegree[course] += 1

        # Topological Sort
        queue = deque()

        # Add the nodes in the queue whose indegree is 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        
        res = []
        while queue: # TC: O(V + E)
            node = queue.popleft()
            res.append(node)

            for neighbor in pre[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(res) == numCourses:
            return res
        else:
            return []

        
            