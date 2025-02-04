# Brute Force: Use an arraylist
# TC: Get: O(n), Put: O(n)

# Optimal:
# TC: O(1)

class Node: # Double Linked List
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0) # Create dummy head node
        self.tail = Node(0, 0) # Create dummy tail node

        self.head.next = self.tail # Connect the head node with tail node
        self.tail.prev = self.head # Connect the tail node with head node

        self.hashMap = {} # Cache (maps key to node)
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hashMap: 
            currNode = self.hashMap[key] # Get node address from the hashMap
            self.remove(currNode)
            self.insert(currNode)

            return currNode.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap: # If the key to put is already inside
            self.remove(self.hashMap[key])
        self.hashMap[key] = Node(key, value)
        self.insert(self.hashMap[key])
        
        if len(self.hashMap) > self.capacity:
            self.remove(self.tail.prev)
            
        return None
    
    def insert(self, newNode): # Add that node in the front(1st) position
        self.hashMap[newNode.key] = newNode
        newNode.next = self.head.next
        newNode.prev = self.head
        newNode.next.prev = newNode
        self.head.next = newNode
        
    
    def remove(self, node): # Remove the node from the last position
        del self.hashMap[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)