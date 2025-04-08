

# Find Angle MBC

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())
ac = math.hypot(ab,bc)

theta_rad = math.asin(ab/ac) 
theta_deg = math.degrees(theta_rad)


# Correct print statement
print(f"{round(theta_deg)}\u00B0")

# SOlution 2

import cmath
import math

ab = int(input())
bc = int(input())

# Represent as complex number vector
z = complex(bc, ab)
theta_rad = cmath.phase(z)
theta_deg = math.degrees(theta_rad)
print(f"{round(theta_deg)}°")


# Solution 3

import math

ab = int(input())
bc = int(input())

# theta = arctangent(opposite / adjacent)
theta = math.degrees(math.atan2(ab, bc))
print(f"{round(theta)}°")
