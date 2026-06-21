# Password Strength Checker

password = input("Enter your password: ")

# Check password length
length = len(password) >= 8

# Check for numbers
has_number = any(char.isdigit() for char in password)

# Check for uppercase letters
has_upper = any(char.isupper() for char in password)

# Check for special characters
special_chars = "@#$!%^&*()_+-=[]{}|;:',.<>?/"
has_special = any(char in special_chars for char in password)

# Calculate strength
score = sum([length, has_number, has_upper, has_special])

print("\nPassword Analysis:")
print("Length >= 8:", length)
print("Contains Number:", has_number)
print("Contains Uppercase:", has_upper)
print("Contains Special Character:", has_special)

# Display password strength
if score == 4:
    print("Password Strength: Strong ")
elif score == 3:
    print("Password Strength: Medium ")
elif score == 2:
    print("Password Strength: Weak ")
else:
    print("Password Strength: Very Weak ")