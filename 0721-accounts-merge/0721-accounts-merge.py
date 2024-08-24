# Disjoint Set Time and Space Complexity
# TC: O(N) + O(4α), here α = constant
# SC: O(N) (parent, size, rank array) 
class DisjointSet:
    def __init__(self, n):
        # self.rank = [0] * (n + 1) # Can be used for 0-based and 1-based indexing 
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n+1)]
        
    def findUltimateParent(self, node):
        # Base Case
        if self.parent[node] == node:
            return node
            
        self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]
        
    # def unionByRank(self, u, v):
    #     ulp_u = self.findUltimateParent(u)
    #     ulp_v = self.findUltimateParent(v)
        
    #     if (ulp_u == ulp_v):
    #         return
        
    #     if self.rank[ulp_u] < self.rank[ulp_v]:
    #         self.parent[ulp_u] = ulp_v
    #     elif self.rank[ulp_u] > self.rank[ulp_v]:
    #         self.parent[ulp_v] = ulp_u
    #     else:
    #         self.parent[ulp_v] = ulp_u
    #         self.rank[ulp_u] += 1
            
    def unionBySize(self, u, v):
        ulp_u = self.findUltimateParent(u)
        ulp_v = self.findUltimateParent(v)
        
        if (ulp_u == ulp_v):
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


# TC: O(N * KlogK) where N is the number of accounts and K is the average number of emails per account.

# SC: O(N * K) where N is the number of accounts and K is the average number of emails per account.

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisjointSet(n)

        mapMailNode = defaultdict(int)
        # Map each email to a node and merge nodes with common emails
        for i in range(n):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if mail not in mapMailNode:
                    mapMailNode[mail] = i
                else:
                    ds.unionBySize(mapMailNode[mail], i)

        # Group emails by their root parent
        emailGroups = defaultdict(list)
        for email, index in mapMailNode.items():
            root = ds.findUltimateParent(index)
            emailGroups[root].append(email)


        # Sort emails and prepare the result in the required format
        result = []
        for node in emailGroups:
            sortedEmails = sorted(emailGroups[node])
            sortedEmails.insert(0, accounts[node][0])  # Insert the name at the first position
            result.append(sortedEmails)

        return result
        





            

        

        
            


        




        
        