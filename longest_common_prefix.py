def longestCommonPrefix(strs):
    for i, letter_group in enumerate(zip(*strs)):
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    else:
        return min(strs)
                

strs = ["flowser","flows","floight"]
print(longestCommonPrefix(strs))