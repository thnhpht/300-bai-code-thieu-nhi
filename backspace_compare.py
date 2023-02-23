def backspaceCompare(s, t):
    while "#" in s:
        if s.index("#") == 0:
            s = s[1:]
            continue
        index_s = s.index("#")
        s = s[:index_s-1] + s[index_s+1:]

    while "#" in t:
        if t.index("#") == 0:
            t = t[1:]
            continue
        index_t = t.index("#")
        t = t[:index_t-1] + t[index_t+1:]
    
    return s == t
        
s = "a##c"
t = "#a#c"


print(backspaceCompare(s, t))