import cv2
import numpy as np

# touch this function, it's not 100% functional
def binary(image):

    height, width  = image.shape

    output = image

    for i in range(height):
        for j in range(width):
            pixel = image[i, j]

            if (pixel < 127):
                output[i, j] = 0
            else:
                output[i, j] = 255

    return output

def count_pixels(image):

    width, height = image.shape
    visited = [[False for j in range(width)] for i in range(height)]

    count = 0

    #Go pixel by pixel
    for i in range(height):
        for j in range(width):

            #If the pixel hasn't been visited yet and it is a black pixel
            if visited[i][j] == False and image[i][j] == 1:

                #print(image[i][j])
                DFS(i,j,visited, image)
                count += 1

    return count


# A utility function to do DFS for a 2D  
# boolean matrix. It only considers 
# the 8 neighbours as adjacent vertices 
def DFS(i, j, visited, image):

    #These 2 arrays are used to get the indices of the surrounding 8 pixels for each pixel
    row =[-1, -1, -1, 0, 0, 1, 1, 1]
    column = [-1, 0, 1, -1, 1, -1, 0, 1]

    visited[i][j] = True
    
    #Check recursively for each neighbor
    for k in range(8):
        if checkBounds(i + row[k],j + column[k],visited,image):
            DFS(i + row[k], j + column[k], visited,image)



def checkBounds(i,j,visited,image):

    #check if row and column are in range
    #check to ensure the pixel has not been visited yet
    #check to ensure that the pixel is black
    
    row, column = image.shape
    
    #Change this 0 to a 1 if you wanna count the number of connected regions based on 1
    return(i >= 0 and i < row and j >= 0 and j < column and not visited[i][j] and image[i][j] == 1)

# returns the average of two numbers x & y
def average(x, y):
    return (x + y) / 2

# scales an image down by half
def minifyScaleByTwo(image):

    # get image dimensions
    height, width  = image.shape
    tHeight = height / 2
    tWidth = width / 2

    # create output image
    output = np.zeros((tHeight, tWidth), np.uint8)
    #output = cv2.resize(output, (tWidth, tHeight))

    for x in range(0, tHeight):
        x2 = x * 2
        print("x2", x2)
        for y in range(0, tWidth):
            y2 = y * 2
            print("y2:", y2)
            p = average(image[x2][y2], image[x2][y2 + 1])
            q = average(image[x2 + 1][y2], image[x2 + 1][y2 + 1])
            output[x][y] = average(p, q)

    output = binary(output)
    print(output)
    return output

def main():

    img = cv2.imread('images/bird.jpg', cv2.IMREAD_GRAYSCALE)
    # img2 = (np.array([
    #         [1, 1, 0, 0, 0], 
    #         [0, 1, 0, 0, 1], 
    #         [1, 0, 0, 1, 1], 
    #         [0, 0, 0, 0, 0], 
    #         [1, 0, 1, 0, 1]
    #     ]))
    
    out = binary(img)
    out = minifyScaleByTwo(img)
    cv2.imshow('image', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # regions = count_pixels(img2)
    # print("There are ", regions, " connected regions")
    return


main()