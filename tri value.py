import math
import random

# Generate a random angle in degrees
angle_deg = random.randint(0, 360)

# Convert degrees to radians
angle_rad = math.radians(angle_deg)

# Calculate trigonometric values
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad)

# Display results
print("Angle (degrees):", angle_deg)
print("Sin:", sin_val)
print("Cos:", cos_val)
print("Tan:", tan_val)
