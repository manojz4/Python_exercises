

################################################################

from datetime import datetime 

obj = datetime(2024,12,29,11,10,9,99)

print(obj.year)
print(obj.month)
print(obj.day)
print(obj.hour)
print(obj.minute)
print(obj.second)


from datetime import date

obj = date(2024,12,29)

print(obj.year)
print(obj.month)
print(obj.day)


from datetime import time

obj = time(11,10,9,99)

print(obj.hour)
print(obj.minute)
print(obj.second)

import math
print(math.sqrt(4))
print(math.pow(2,3))

# import os 
# cwd = os.getcwd() 
# print("Current working directory:", cwd) 
