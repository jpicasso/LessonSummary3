
# Create a Temperature converter, Celsius to Fahrenheit:
# 0 degrees Celsius is equal to 32 degrees Fahrenheit:
# 0 °C = 32 °F
# The temperature T in degrees Fahrenheit (°F) is equal to the temperature T in degrees Celsius (°C) times 9/5 plus 32:
# T(°F) = T(°C) × 9/5 + 32

# Example:
# Convert 20 degrees Celsius to degrees Fahrenheit:
# T(°F) = 20°C × 9/5 + 32 = 68 °F

# Add:
# if Fahrenheit is more than 90, print statement "a heat warning", if Fahrenheit is less than 30, print statement "a cold warning"

user_input = float(input('Enter temperature in Celsius: '))
output = user_input*1.8 + 32
if output >90:
  print('A heat warning. Temp is {} Fahrenheit' .format(output))
elif output <30:
  print('A cold warning. Temp is {} Fahrenheit' .format(output))
else:
  print('Temp is {} Fahrenheit' .format(output))
  
