import random
import string

# characters to generate the password
chars = list(string.ascii_letters + string.digits + string.punctuation)

# ask the user if they want to generate a password 
response = input("do you want to generate a password? (yes/no): ")

# if the response is yes, generate it after asking how long the length should be 
if response.lower() == 'yes':
    length = int(input("how long should the password be? (enter number) "))
    
    password = ''.join(random.choice(chars) for _ in range(length))
    
    # print the generated password
    print("Generated password:", password)
# if user says no
else:
    print("thats ok!! no password generated")