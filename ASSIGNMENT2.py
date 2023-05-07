import random

# Define a threshold for temperature and humidity
TEMP_THRESHOLD = 30 # in Celsius
HUMIDITY_THRESHOLD = 30 # percent

# Generate a random temperature value between 20 and 50 degrees Celsius
temperature = round(random.uniform(20, 50), 1)
print("Temperature:", temperature, "C")

# Generate a random humidity value between 20 and 50 percent
humidity = round(random.uniform(20, 50), 1)
print("Humidity:", humidity, "%")

# Check if the temperature or humidity exceeds the threshold and trigger an alarm if true
if temperature > TEMP_THRESHOLD:
   print("High temperature detected!")
   print("Alarm on")
else:
    print('Alarm off')
    # code to play alarm sound goes here
if humidity > HUMIDITY_THRESHOLD:
    print("High humidity detected!")
    print("Alarm on")

else:
    print('Alarm off')
    # code to play alarm sound goes here
