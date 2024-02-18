""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:41:24 
"""

""" EXERCISE 04
    4.(f) Installing and usage of standard library modules.
"""

# Importing standard library module
import math

print("Square root of 25:", math.sqrt(25))

# Importing installed module using # !pip install requests
import requests

# Using installed module
response = requests.get('https://www.example.com')
print("Status code of example.com:", response.status_code) 


""" --------------[OUTPUT]--------------------

Square root of 25: 5.0
Status code of example.com: 200

--------------[END-OF-OUTPUT]-------------- """
