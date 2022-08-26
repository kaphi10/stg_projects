import math
 
# function to calculate LCM
def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm
 
 
# array of integers
arr1 = [1,2,3,4]
arr2 = [2,3,4,5]
arr3 = [3,4,5,6]
arr4 = [2,4,6,8,10]
arr5 = [8,4,12,40,26,28,30]
 
print("LCM of arr1 elements:", LCMofArray(arr1))
print("LCM of arr2 elements:", LCMofArray(arr2))
print("LCM of arr3 elements:", LCMofArray(arr3))
print("LCM of arr4 elements:", LCMofArray(arr4))
print("LCM of arr5 elements:", LCMofArray(arr5))
