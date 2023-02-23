def romanToInt(s):
    convert = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0

    for i in range(len(s)):
        if i != len(s) - 1:
            if s[i] == "I":
                if s[i+1] == "V" or s[i+1] == "X":
                    res -= 1
                    continue
            elif s[i] == "X":
                if s[i+1] == "L" or s[i+1] == "C":
                    res -= 10   
                    continue 
            elif s[i] == "C":
                if s[i+1] == "D" or s[i+1] == "M":
                    res -= 100
                    continue
        res += convert[s[i]]
    return res

s = "LVIII"
print(romanToInt(s))