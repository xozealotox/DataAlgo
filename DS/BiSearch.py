class Solution(object):

    def BiSearch(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            middle = left + ((right - left) >> 1)
            print(left, right, middle)
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle

        return right


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    target = 10
    s = Solution()
    ret = s.BiSearch(arr, target)
    print(ret)
