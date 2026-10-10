#TO check if a string is a palindrome or not 

s=input("Enter a string: ")

s=s.lower().replace(" ","")  # Convert to lowercase and remove spaces   

if s==s[::-1]:
    print("The string is a palindrome.")    
else:
    print("The string is not a palindrome.")