image = [[0,0,0],[0,0,0]]
sr = 1
sc = 0
color = 2

def floodFill(image, sr, sc, color):
    try:
        if image[sr-1][sc] == image[sr][sc]:
            for i in range(-1, 2):
                try:
                    image[sr-1][sc+i] = color
                except:
                    pass
    except:
        pass

    try:
        if image[sr][sc+1] == image[sr][sc]:
            for i in range(-1, 2):
                try:
                    image[sr+1][sc+i] = color
                except:
                    pass
    except:
        pass

    try:
        if image[sr+1][sc] == image[sr][sc]:
            for i in range(-1, 2):
                try:
                    image[sr+1][sc+i] = color
                except:
                    pass
    except:
        pass

    try:
        if image[sr][sc-1] == image[sr][sc]:
            for i in range(-1, 2):
                try:
                    image[sr+i][sc-1] = color
                except:
                    pass
    except:
        pass
    
    image[sr][sc] = color
    return image

print(floodFill(image, sr, sc, color))