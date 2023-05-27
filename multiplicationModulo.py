from mpmath import mp

# Set the desired precision (number of decimal places)
precision = 9999

# Set the working precision of mpmath
mp.dps = precision

# Calculate Pi with the desired precision
pi = mp.pi

# Print Pi with the specified precision
print(f"Pi: {pi}")
