def hammingWeight(n):
    return bin(n).count("1")
    
n = 1011
print(hammingWeight(n))