""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:43:38 
"""

""" EXERCISE 10
    10.(d) Apply else and finally clauses.
"""

try:
    file = open("example.txt", "r")
    contents = file.read()
    print("File contents:", contents)

except FileNotFoundError:
    print("File not found.")

else:
    print("File read successfully.")

finally:
    if 'file' in locals():
        file.close()
        print("File closed.")


""" --------------[OUTPUT]--------------------

File not found.

--------------[END-OF-OUTPUT]-------------- """
