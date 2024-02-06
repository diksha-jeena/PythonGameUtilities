import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    passLen = int(input("Enter password length\n"))
    customization = input("Enter any customization you want (name/number): ")

    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    
    random.shuffle(s)
    
    # Generate a password without customization
    password = "".join(s[0:passLen])
    
    if customization.lower() == 'name':
        # Allow the user to input their name
        name_input = input("Enter your name: ")
        password = name_input + password
    elif customization.lower() == 'number':
        # Allow the user to input a number
        number_input = input("Enter a number: ")
        password = number_input + password
    
    print("Your password is:", password)
