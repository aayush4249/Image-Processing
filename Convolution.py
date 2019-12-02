import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)

#Assignments 1 and 3


#Flip the kernel
def conv_transform(kernel):
    kernel_copy = kernel.copy()

    for i in range(kernel.shape[0]):

        for j in range(kernel.shape[1]):
            kernel_copy[i][j] = kernel[kernel.shape[0] -
                                       i-1][kernel.shape[1]-j-1]

    return kernel_copy

#Convolute
def conv(img,filter):

    kernel = conv_transform(filter)
    img_row,img_col=img.shape
    ker_row,ker_col=kernel.shape
    #if ker_row!=ker_col:
    #   print("no of rows and column of kernel/mask should equal")
    #    return
    out=np.zeros((img_row,img_col))
    
    img = padd(img, kernel)  #Padd the array to calculate new dimensions

    #Apply convolution, use sliding window method and go pixel by pixel
    for a in range(img_row):
        for b in range(img_col):
            for c in range(ker_row):
                for d in range(ker_col):
                    out[a,b] = out[a,b]+(kernel[c,d]*img[a+c,b+d])

    return out

#Padding
def padd(img,kernel):
    r,c = img.shape
    kr,kc = kernel.shape
    padded = np.zeros((r+kr,c+kc),dtype=img.dtype)
    insert = np.uint((kr)/2)
    padded[insert:insert+r,insert:insert+c] = img #Populate already existing values
    return padded



def main():

    filter_sharpen = (np.array([
        [0, -1, 0],
       	[-1, 5, -1],
       	[0, -1, 0]
    ]))

    filter_sobel_bottom = (np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]))
    
    filter_edge_detection = (np.array([
    	[1, 0, -1],
    	[0, 0, 0],
    	[-1, 0, 1]
    ]))


    filter_blur =  (1/(3*3))*np.ones((3, 3), dtype=np.float64)


    #A1 stuff comment this out when running A3
    #'''
    img = cv2.imread('Images/dog.png', cv2.IMREAD_GRAYSCALE) / 255
   
    convoluted = conv(img, filter_sharpen)
    #cv2.imshow('Original', img)
    #cv2.imshow("Filtered",convoluted)
    horizontal_stack = np.hstack((img,convoluted))
    cv2.imshow("Original Vs. Filtered",horizontal_stack)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #'''

    #A3 Stuff comment this out when running A1
    '''
    filter_A3_1 = (1/3)*np.ones((1, 3), dtype=np.float64)

    filter_A3_2 = (1/3)*np.ones((3, 1), dtype=np.float64)

    filter_1 = (np.array([
        [1/3, 1/3, 1/3], 
    ]))

    filter_2 = (np.array([
        [1/3],
        [1/3],
    	[1/3]
    ]))
    
    img = cv2.imread("Images/dog.png", cv2.IMREAD_GRAYSCALE) / 255
    convoluted = conv(img, filter_1)
    convoluted2 = conv(convoluted,filter_2)
    convoluted3 = conv(img,filter_blur)
    horizontal_stack = np.hstack((img,convoluted2))
    horizontal_stack = np.hstack((horizontal_stack,convoluted3))
    cv2.imshow('Original Vs. 1/3 and 1/3 Vs. 1/9', horizontal_stack)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()
    '''

 

    return


main()
