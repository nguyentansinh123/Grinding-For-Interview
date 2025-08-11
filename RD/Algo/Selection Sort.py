
def sort(nums):

    for i in range(len(nums)):

        minposition = i 

        for j in range(i, len(nums)):
            if nums[j] < nums[minposition]:
                minposition = j 
        
        nums[i], nums[minposition] = nums[minposition], nums[i]
    

         

nums = [5,3,8,7,2]
sort(nums)
print(nums)
