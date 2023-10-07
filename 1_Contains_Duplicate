class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        track = []

        for i in range(0, len(nums)):
            if nums[i] in track:
                return True
            else:
                track.append(nums[i])

        return False
