def climbStairs(n):
    return int(round(1/5**0.5 * (((1+5**0.5)/2.0)**(n+1) - ((1-5**0.5)/2.0)**(n+1))))

print(climbStairs(7))