import sys
class Palindrome:

    def __init__(self, *args):
        stub = list()
        if len(args) > 0:
            for x in args:
                stub.append(x)
            self.wordlength = stub[0]
            self.alphabetlength = stub[1]
            self.numberlength = stub[2]
            self.specialcharlength = stub[3]
        else:
            self.wordlength = int(input("Input word length wordlength:"))
            self.alphabetlength = int(input("Input Alphabet length alphabetlength:"))
            self.numberlength = int(input("Input Number length numberlength:"))
            self.specialcharlength = int(input("Input Special char length specialcharlength:"))

    def formpalindrome(self):
        """ Function Forms a palindrome (where its word length 'w')
            which has 'x' number of alphabets,
            'y' number of digits & 'z' number of special characters
            where w, x, y and z can be input from the userFunction to form a palindrome
        """

        maxlength = 20
        oddcount = (self.alphabetlength % 2 + self.numberlength % 2 + self.specialcharlength % 2)
        # print("Odd count = ", oddcount)

        # validation of the inputs

        if self.wordlength > maxlength:
            print(self.wordlength, "Word length exceeds max allowed length : ", maxlength)
            return(False)

        if self.wordlength < 0:
            print(self.wordlength, "Word length is less than 0")
            exit(1)

        if self.alphabetlength > self.wordlength:
            print(self.alphabetlength, "Albhabets more than word length: ", self.wordlength)
            exit(1)

        if self.alphabetlength < 0:
            print(self.alphabetlength, "Albhabets less than 0: ")
            exit(1)

        if self.numberlength > self.wordlength:
            print(self.numberlength, "Numbers more than word length: ", self.wordlength)
            exit(1)

        if self.numberlength < 0:
            print(self.numberlength, "Numbers less than 0: ", self.numberlength)
            exit(1)

        if self.numberlength > self.wordlength:
            print(self.specialcharlength, "Special chars more than word length: ", self.wordlength)
            exit(1)

        if self.specialcharlength < 0:
            print(self.specialcharlength, "Special Chars less than 0: ")
            exit(1)

        if (self.alphabetlength + self.numberlength + self.specialcharlength) != self.wordlength:
            print("x = %d, y = %d, z = %d does not add up to w = %d\n" % (
            self.alphabetlength, self.numberlength, self.specialcharlength, self.wordlength))
            exit(1)

        if oddcount > 1:
            print("Input is not valid to create a Palindrome")
            print("Error: Cannot create palindrome as more than 1 odd set: ", oddcount)
            exit(1)

        # identify the mid from the arg that has odd value
        mid = ''
        if (self.alphabetlength % 2) == 1:
            mid = "a"
        if (self.numberlength % 2) == 1:
            mid = "1"
        if self.specialcharlength % 2 == 1:
            mid = "*"
        # print("mid=",mid)

        # Form half string
        i = 0
        j = 0
        k = 0
        halfpal = ''
        while i < (self.alphabetlength // 2):
            halfpal = halfpal + chr(65 + i)
            i = i + 1
        # print(halfpal)

        while j < (self.numberlength // 2):
            halfpal = halfpal + chr(48 + j)
            j = j + 1
        # print(halfpal)

        while k < (self.specialcharlength // 2):
            halfpal = halfpal + chr(33 + k)
            k = k + 1
        # print(halfpal)

        # Form reverse of the half string
        revpal = halfpal[::-1]

        # Form the final string
        pal = halfpal + mid + revpal
        return pal

