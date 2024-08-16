# Note: Can solve the question using 2 ways
# 1) Detect if a directed graph has a cycle (using DFS)
# 2) Topological Sort (using BFS)


# Topological Sort 
# TC: O(V + E), V = number of courses
# SC: O(number of courses)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Create adjacency list
        pre = defaultdict(list)
        for course, prerequisite in prerequisites:
            pre[course].append(prerequisite)

        # Topological Sort

        queue = deque()
        indegree = [0] * numCourses

        # Calculate the indegree for each node
        for node in pre:
            for neighbor in pre[node]:
                indegree[neighbor] += 1

        # Add the nodes in the queue whose indegree is 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        courses = 0
        while queue:
            node = queue.popleft()
            courses += 1

            for neighbor in pre[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if courses == numCourses:
            return True
        else:
            return False



            

        