import unittest
import Palindrome as PalindromeClass
import re


class TestCaseToCheckGivenStringIsPalindrome(unittest.TestCase):
    def test_IsPalindromeWithNoSpecialCharacter(self):
        formedpalindrome = PalindromeClass.Palindrome(6, 4, 2, 0)
        palindromestring = formedpalindrome.formpalindrome()
        print(palindromestring)
        if palindromestring == palindromestring[::-1]:
            ispalindrome = True
        else:
            ispalindrome = False
        specialcharactercheck = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if specialcharactercheck.search(palindromestring) is None:
            noSpecialCharacter = True
        else:
            noSpecialCharacter = False
        self.assertTrue(ispalindrome & noSpecialCharacter)

    def test_IsPalindromeWithNoNumber(self):
        formedpalindrome = PalindromeClass.Palindrome(6, 4, 0, 2)
        palindromestring = formedpalindrome.formpalindrome()
        print(palindromestring)
        if palindromestring == palindromestring[::-1]:
            ispalindrome = True
        else:
            ispalindrome = False
        numbercheck = re.compile('[0123456789]')
        if numbercheck.search(palindromestring) is None:
            noNumbers = True
        else:
            noNumbers = False
        self.assertTrue(ispalindrome & noNumbers)

    def test_IsPalindromeWithNoAlphabet(self):
        formedpalindrome = PalindromeClass.Palindrome(6, 0, 2, 4)
        palindromestring = formedpalindrome.formpalindrome()
        print(palindromestring)
        if palindromestring == palindromestring[::-1]:
            ispalindrome = True
        else:
            ispalindrome = False
        alphabetcheck = re.compile('[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]')
        if alphabetcheck.search(palindromestring) is None:
            noAlphabets = True
        else:
            noAlphabets = False
        self.assertTrue(ispalindrome & noAlphabets)

    def test_IsPalindromeWithNoNumberAndSpecialCharacter(self):
        formedpalindrome = PalindromeClass.Palindrome(6, 6, 0, 0)
        palindromestring = formedpalindrome.formpalindrome()
        print(palindromestring)
        if palindromestring == palindromestring[::-1]:
            ispalindrome = True
        else:
            ispalindrome = False
        nonumberandnospecialcharactercheck = re.compile('[0123456789@_!#$%^&*()<>?/\|}{~:]')
        if nonumberandnospecialcharactercheck.search(palindromestring) is None:
            noNumberandnoSpecialCharacter = True
        else:
            noNumberandnoSpecialCharacter = False
        self.assertTrue(ispalindrome & noNumberandnoSpecialCharacter)

    def test_IsWordGreaterthan20(self):
        formedpalindrome = PalindromeClass.Palindrome(21, 6, 0, 0)
        palindromestring = formedpalindrome.formpalindrome()
        self.assertFalse(palindromestring)
       
if __name__ == '__main__':
    unittest.main()
