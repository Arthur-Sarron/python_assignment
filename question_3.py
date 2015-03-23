text = input("enter your word\n")

if text[::-1] == text:
    print(text,"is a palindrome")
else: 
    print(text,"isn't a palindrome")
