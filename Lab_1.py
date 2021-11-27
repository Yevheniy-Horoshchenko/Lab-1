from math import sqrt
from math import fabs
def err(x1,x2):
    delx1 = (abs(x1-x2)/x1)
    return delx1
    
dl1 = err(round(sqrt(74),2),8.60233)
dl2 = err(round(12/11,2),1.09091)

if (dl1 > dl2):
   print("First number is more precisely!", dl1)
else:
   ("Second number is more precisely!", dl2)
