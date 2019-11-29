import cv2
import numpy as np


#Assignments 5 and 6

def main():

    #Go through all images and get their feature vectors, then save to file
    f = open("Vectors.txt","w")
    img = cv2.imread("Images/0.png", cv2.IMREAD_GRAYSCALE)
    binary_image = binary(img)
    vector = get_vector(binary_image)
    print(vector, file =f)
    
    for x in range(1,10):
        img = cv2.imread("Images/"+str(x)+"-1.png", cv2.IMREAD_GRAYSCALE)
        binary_image = binary(img)
        vector = get_vector(binary_image)
        print(vector, file =f)
    
    f.close()
    return

#Convert Image to Black and White
def binary(image):

    height, width = image.shape
    output = image

    for i in range(height):
        for j in range(width):
            pixel = image[i, j]

            if (pixel < 128):
                output[i, j] = 0
            else:
                output[i, j] = 255

    return output


def get_vector(img):

    rows = img.shape[0]
    columns = img.shape[1]
    x = [None] * 4
    y = [None] * 4
    vector = [None] * 9
    black = 0 
    white = 0
    
    #Turn into 1d array
    flat = img.ravel()
    
    #4 vertical lines, 3 columns
    #Results in 3x3 grid
    for i in range(4):
        x[i] = (columns/3)*i
        y[i] = (rows/3)*i
    
    #Go through each cell in grid
    for i in range(9):

        #Identify row
        for j in range(int(y[i//3]), int(y[i//3 + 1])):
            
            #Identify column
            for k in range(int(x[i%3]),int(x[i%3 + 1])):
                
                if flat[columns*j + k] >=1:
                    white+=1
                else:
                    black+=1
        
        #Get Ratio of black to white
        vector[i] = black/white
        black = 0
        white = 0

    return vector

main()
