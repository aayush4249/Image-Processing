import numpy as np 
import cv2



def main():

    img = cv2.imread("Images/nice.jpg", 0) 
    img2 = cv2.imread("Images/quote.jpg", 0) 


    img_sized = cv2.resize(img, (400, 400))
    img2_sized = cv2.resize(img2, (400, 400))

    combined  = np.zeros(shape=(400,400))

    #Combine the images
    for i in range(400):
        for j in range(400):
            combined[i][j] = img_sized[i][j] & img2_sized[i][j]
    
    final = reduceNoise(combined)
    cv2.imwrite("Images/combined.jpg", final)
    
    
    img3 = cv2.imread("Images/combined.jpg")
    
    cv2.imshow('Combined Image', img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return

def reduceNoise(img):
    
    #Uses a 3x3 filter to remove noise from the image
    row, col = img.shape 
    newImg = np.zeros((row, col))
    
    for i in range(1, row - 2):
        
        for j in range(1, col-2):

            win = []
            
            #Goes through 3 rows
            for x in range(i - 2, i + 3):
                
                #Goes through 3 columns
                for y in range(j - 2, j + 3):
                    
                    win.append(img[x][y])
            
            #sort the values
            win.sort()
            
            #Take the center pixel which is 4 in a 3x3 hood
            newImg[i][j] = win[12]
    
    return newImg

'''

row,col = img.shape
    newImg = np.zeros((row,col))
    
    for i in range(1, row - 2):
        
        for j in range(1, col-2):

            win = []
            
            #Goes through 5 rows
            for x in range(i-2,i+3):
                
                #Goes through 5 columns
                for y in range(j-2,j+3):
                    
                    win.append(img[x][y])
            
            #sort the values
            win.sort()
            
            #Take the center pixel which is 12 in a 5x5 hood
            newImg[i][j] = win[12]

'''


main()
