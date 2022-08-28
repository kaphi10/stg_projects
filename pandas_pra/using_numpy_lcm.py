import numpy as np
 
ev=list(range(2,102,2))
output=np.lcm.reduce(ev)
print("the LCM of even number from 1-100 including the numbers is",output)