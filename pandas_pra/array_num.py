import numpy as np
import math 
# list_num= np.arange(5.5,20.5,0.5).toarray()
# print(list_num)
li=list(range(1,101))
ar=np.array(li)
def LcmofArray(a):
    lcm=a[0]
    for i in range(0,len(a)):
        lcm = lcm*a[i]//math.gcd(lcm, a[i])
    return lcm
even_num=list(filter(lambda x:x%2==0,li))
# ev=list(range(2,102,2))
# ar2=np.array(ev)
#print(ar2)
print("lcm of array of even numbers from 1-100 is ",LcmofArray(even_num))