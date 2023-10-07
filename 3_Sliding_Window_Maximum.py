class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        dq = collections.deque()
        ans = []

        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)
            
            if l > dq[0]:
                dq.popleft()

            if r >= k-1:
                ans.append(nums[dq[0]])
                l+=1

            r+=1

        return ans
