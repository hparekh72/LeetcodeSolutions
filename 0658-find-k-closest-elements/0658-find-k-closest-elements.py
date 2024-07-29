class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # Brute Force: Sorting
        # TC: O(nlogn) + O(nlogn)

        closest_sorted_arr = sorted(arr, key=lambda num: (abs(x - num), num))
        
        return sorted(closest_sorted_arr[:k])