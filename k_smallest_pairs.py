class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        import heapq

        def solve(a, b, k):
            if not a or not b or k == 0: return []
            if len(a) * len(b) <= k: return sorted(((x, y) for x in a for y in b), key=sum)
            res, h, t, count = [], [], set(), 0
            heapq.heappush(h, (a[0] + b[0], 0, 0))
            t.add((0, 0))
            while count < k:
                s, i, j = heapq.heappop(h)
                res.append((a[i], b[j]))
                count += 1
                for i, j in [(i + 1, j), (i, j + 1)]:
                    if i < len(a) and j < len(b) and not (i, j) in t:
                        heapq.heappush(h, (a[i] + b[j], i, j))
                        t.add((i, j))
                
            return res

        return solve(nums1, nums2, k)
    


            

    
        
