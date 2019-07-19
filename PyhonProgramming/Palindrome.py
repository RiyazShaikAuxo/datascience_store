stirng1=input("Enter the string: ")
stirng1=stirng1.casefold()
rev_stng=reversed(stirng1)
if list(stirng1)==list(rev_stng):
    print("The string is plaindromed")
else:
    print("The string is not palindromed one")