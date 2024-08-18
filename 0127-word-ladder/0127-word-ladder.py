# Graph BFS Implementation
# TC: O(len(wordList)) * O(len(word[0])) * 26
# SC: O(len(wordList)) (hashSet) +  O(len(wordList)) (queue)


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append((beginWord, 1)) # Add the beginWord and step count in the queue

        # Convert the wordList into a set for faster lookup
        hashSet = set(wordList)

        # Remove the beginWord from the set if present (acts as marking visited)
        hashSet.discard(beginWord) 

        # Perform BFS on the word ladder graph
        while queue:
            word, steps = queue.popleft()
            
            # Check if the current word is the endWord
            if word == endWord:
                return steps

            word = list(word)
            # Iterate through each character in the current word
            for i in range(len(word)):
                originalChar = word[i]

                # Try replacing the current character with every possible lowercase alphabet
                for j in range(ord('a'), ord('z') + 1): # 'a' -> 'z'. 26 characters
                    word[i] = chr(j) 
                    s = "".join(word)

                    if s in hashSet:
                        queue.append((s, steps + 1))
                        hashSet.remove(s)  # Remove the word from the set to mark as visited
                
                # Restore the original character
                word[i] = originalChar
        
        return 0


