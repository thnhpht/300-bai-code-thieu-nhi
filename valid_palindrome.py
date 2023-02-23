def isPalindrome(s):
    new_s = [x.lower() for x in s if x.isalnum()]
    return new_s == new_s[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))