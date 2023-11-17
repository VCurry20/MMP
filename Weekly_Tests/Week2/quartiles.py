# quartiles
# https://www.educative.io/answers/basic-statistics-using-python





def quartiles(nums):
    nums=sorted(nums)
    Q1 = median(nums[:len(nums)//2])
    Q2 = median(nums)
    if len(nums)%2 == 0:
        Q3 = median(nums[len(nums)//2:])
    else:
        Q3 = median(nums[len(nums)//2+1:])
    return Q1,Q2,Q3


def median(nums):
    nums.sort()
    if len(nums)%2 == 0:

        return int(nums[len(nums)//2-1]+nums[len(nums)//2])/2
    else:
        return nums[len(nums)//2]

a =[11, 21, 34, 22, 27, 11, 23, 21]
print (quartiles(a))