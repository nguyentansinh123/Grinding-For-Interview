
def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):

            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


nums = [2,5,8,3,6,9,23] 
sort(nums)
print(nums)