
def sort(nums):

    for i in range(1, len(nums)):
        j = i 

        while nums[j -1] > nums[j] and j > 0:
            nums[j - 1], nums[j] = nums[j], nums[j-1]
            j-= 1

         

nums = [5,3,8,7,2]
sort(nums)
print(nums)
