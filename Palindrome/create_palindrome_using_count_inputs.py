# Function to form a palindrome from user input of count
def formpalindrome(wordlength, alphabetlength, numberlength, specialcharlength):
    """ Function returns a palindrome (where its word length 'w')
        which has 'x' number of alphabets,
        'y' number of digits & 'z' number of special characters 
        where w, x, y and z can be input from the userFunction to form a palindrome 
    """
    maxlength = 20
    oddcount = (alphabetlength % 2) + (numberlength % 2) + (specialcharlength % 2)
    #print("Odd count = ", oddcount)
    
    #Validation of the inputs
  
    if wordlength > maxlength:
        print(wordlength, "Word length exceeds max allowed length : ", maxlength)
        exit(1)

    if wordlength <= 0:
        print(wordlength, "Word length is less than or equal to 0")
        exit(1)

    if alphabetlength > wordlength:
        print(alphabetlength, "Albhabets more than word length: ", wordlength)
        exit(1)

    if alphabetlength < 0:
        print(alphabetlength, "Albhabets less than or equal to 0: ")
        exit(1)

    if numberlength > wordlength:
        print(numberlength, "Numbers more than word length: ", wordlength)
        exit(1)

    if numberlength < 0:
        print(numberlength, "Numbers less than or equal to 0: ", numberlength)
        exit(1)

    if numberlength > wordlength:
        print(specialcharlength, "Special chars more than word length: ", wordlength)
        exit(1)

    if specialcharlength < 0:
        print(specialcharlength, "Special Chars less than or equal to 0: ")
        exit(1)

    if (alphabetlength + numberlength + specialcharlength) != wordlength:
        print("x = %d, y = %d, z = %d does not add up to w = %d\n" % (alphabetlength,numberlength,specialcharlength,wordlength))
        exit(1)

    if oddcount > 1:
        print("Input is not valid to create a Palindrome")
        print("Error: Cannot create palindrome as more than 1 odd set: ",oddcount)
        exit(1)

    #Identify the mid from the arg that has odd value
    mid=''
    if (alphabetlength % 2) == 1:
        mid = "a"
    if (numberlength % 2) == 1:
        mid = "1"
    if (specialcharlength % 2) == 1:
        mid = "*"
    #print("mid=",mid)
    
    #Form half string
    i=0
    j=0
    k=0
    halfpal=''
    while i < (alphabetlength // 2):
        halfpal = halfpal + chr(65 + i)
        i=i+1
    #print("First half of palindrome with aplhabet: ", halfpal)
    
    while j < (numberlength // 2):
        halfpal = halfpal + chr(48 + j)
        j=j+1
    #print("First half of palindrome with aplhabet + number: ",halfpal)
    
    while k < (specialcharlength // 2):
        halfpal = halfpal + chr(33 + k)
        k=k+1
    #print("First half of palindrome with aplhabet + number + specialchar: "halfpal)
    
    #Form reverse of the half string
    revpal = halfpal[::-1]
    
    #Form the final Palindrome string 
    pal = halfpal + mid + revpal
    return(pal)


# Calling the function
def main():

    wordlength = int(input("Input word length w:"))
    alphabetlength = int(input("Input Alphabet length x:"))
    numberlength = int(input("Input Number length y:"))
    speciallength = int(input("Input Special char length z:"))
    pal_val = formpalindrome(wordlength, alphabetlength, numberlength, speciallength)
    if(pal_val):
        print("Palindrome: ", pal_val)
    else:
        print("Input is not valid to create a Palindrome")

main()
