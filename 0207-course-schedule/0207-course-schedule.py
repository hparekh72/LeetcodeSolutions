# Topological Sort 
# TC: O(V + E)
# SC: O(number of courses)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Create adjacency list
        pre = defaultdict(list)
        for course, prerequisite in prerequisites:
            pre[course].append(prerequisite)

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

        while queue:
            node = queue.popleft()
            for neighbor in pre[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        for i in range(len(indegree)):
            if indegree[i] > 0: # If there is a cycle in the graph
                return False
        
        return True

            

        