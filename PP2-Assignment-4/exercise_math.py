## Python Math library

1. Write a Python program to convert degree to radian.
```
Input degree: 15
Output radian: 0.261904
```
import math
degree = 15
radian = math.radians(degree)
print(radian)





2. Write a Python program to calculate the area of a trapezoid.
```
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
```

height = 5
base1 = 5
base2 = 6
area = ((base1 + base2) / 2) * height
print(area)



3. Write a Python program to calculate the area of regular polygon.
```
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
```


import math
sides = 4
length = 25
area = ((sides*length**2)/(4*math.tan(math.pi/sides)))
area= int(area)
print(area)



4. Write a Python program to calculate the area of a parallelogram. 
```
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
```
import math
height = 6
base = 5
area = float ( base*height)
print(area)
