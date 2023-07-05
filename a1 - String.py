# String

# Single Quote
user = 'Hello World!'
print(user) # Output : Hello World!

# Double Quote
user = "Hello World!"
print(user) # Output : Hello World!

# Quotes
print('"Hello World!"') # Output : "Hello World!"
print("'Hello World!'") # Output : 'Hello World!'
print("It's 9 o'clock!") # Output : It's 9 o'clock!

# Backslash
print('It\'s 9 o\'clock!') # Output : It's 9 o'clock!
print("C:\\User\\asus\\Program Files") # Output : C:\User\asus\Program Files

# Tab
print("Purwokerto \tJakarta") # Output : Purwokerto      Jakarta

# Backspace
print("JKT \b48") # Output : JKT48

# Newline
print("Hello \nWorld!") # Output : Hello \n World!
print("Hello \rWorld!") # Output : World!

# Raw String
print(r'D:\User\asus\Coding') # Output : D:\User\asus\Coding

# Multiline String
print("""
Name : Bill Gates
Company : Microsoft
""")

# Output :
# Name : Bill Gates
# Company : Microsoft

# Multiline String and RAW
print(r"""
Name : Steve Jobs
Company : Microsoft
Website : www.microsoft.com/
""")

# Output :
#
# Name : Steve Jobs
# Company : Microsoft
# Website : www.microsoft.com/

# Mengatur Lebar
user = "Aokuri"
string = f"Lebar : {user:>10}"
print(string) # Output : Lebar :     Aokuri
