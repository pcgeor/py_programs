# Function to form a palindrome from user input of count
def FormPalindrome(w, x, y, z):
    """ Function Forms a palindrome (where its word length 'w')
        which has 'x' number of alphabets,
        'y' number of digits & 'z' number of special characters 
        where w, x, y and z can be input from the userFunction to form a palindrome 
    """
    maxlength = 20
    oddcount = (x%2 + y%2 + z%2)
    #print("Odd count = ", oddcount)
    
    # validation of the inputs
  
    if (w > maxlength):
        print(w, "Word length exceeds max allowed length : ", maxlength)
        exit(1)

    if (w < 0):
        print(w, "Word length is less than 0")
        exit(1)

    if (x > w):
        print(x, "Albhabets more than word length: ", w)
        exit(1)

    if (x < 0):
        print(x, "Albhabets less than 0: ")
        exit(1)

    if (y > w):
        print(y, "Numbers more than word length: ", w)
        exit(1)

    if (y < 0):
        print(y, "Numbers less than 0: ", y)
        exit(1)

    if (y > w):
        print(z, "Special chars more than word length: ", w)
        exit(1)

    if (z < 0):
        print(z, "Special Chars less than 0: ")
        exit(1)

    if ((x+y+z) != w):
        print("x = %d, y = %d, z = %d does not add up to w = %d\n" % (x,y,z,w))
        exit(1)

    if (oddcount > 1):
        print("Input is not valid to create a Palindrome")
        print("Error: Cannot create palindrome as more than 1 odd set: ",oddcount)
        exit(1)

    # identify the mid from the arg that has odd value
    mid=''
    if ((x%2) == 1):
        mid="a"
    if ((y%2) == 1):
        mid="1"
    if ((z%2 == 1)):
        mid="*"
    #print("mid=",mid)
    
    #Form half string
    i=0
    j=0
    k=0
    halfpal=''
    while (i < (x//2)):
        halfpal = halfpal + chr(65+i)
        i=i+1
    #print(halfpal)
    
    while (j < (y//2)):
        halfpal = halfpal + chr(48+j)
        j=j+1
    #print(halfpal)
    
    while (k < (z//2)):
        halfpal = halfpal + chr(33+k)
        k=k+1
    #print(halfpal)
    
    #Form reverse of the half string
    revpal = halfpal[::-1]
    
    #Form the final string 
    pal = halfpal + mid + revpal
    return(pal)


# Calling the function
def main():

    w = int(input("Input word length w:"))
    x = int(input("Input Alphabet length x:"))
    y = int(input("Input Number length y:"))
    z = int(input("Input Special char length z:"))
    pal_val = FormPalindrome(w, x, y, z)
    if(pal_val):
        print("Palindrome: ", pal_val)
    else:
        print("Input is not valid to create a Palindrome")

main()
