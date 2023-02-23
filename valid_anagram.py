def isAnagram(s, t):

    if len(s) == len(t):
        while s != "":
            if list(s).count(list(s)[0]) == list(t).count(list(s)[0]):
                s_remove = list(s)[0]
                s = s.replace(s_remove, "")
                t = t.replace(s_remove, "")
            else:
                return False
    else:
        return False

    return True

# def isAnagram(s, t):
#     a = len(s)
#     if a != len(t):
#         return False

#     chars = [0] * 26

#     for i in range(a):
#         chars[ord(s[i]) - ord('a')] += 1
#         chars[ord(t[i]) - ord('a')] -= 1

#     for i in range(26):
#         if chars[i]!=0:
#             return False

#     return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
