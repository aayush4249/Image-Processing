import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)

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

    m,n=img.shape
    p,q=kernel.shape
    if p!=q:
        print("no of rows and column of kernel/mask should equal")
        return
    out=np.zeros((m,n))
    
    img = padd(img, kernel)  # Create new array for final image size
    for a in range(m):
        for b in range(n):
            for c in range(p):
                for d in range(q):
                    out[a,b] = out[a,b]+(kernel[c,d]*img[a+c,b+d])

    print(out)
    return out

def padd(img,kernel):
    r,c = img.shape
    kr,kc = kernel.shape
    padded = np.zeros((r+kr,c+kc),dtype=img.dtype)
    insert = np.uint((kr)/2)
    padded[insert:insert+r,insert:insert+c] = img
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

    img = cv2.imread('dog.png', cv2.IMREAD_GRAYSCALE) / 255
    #img = (np.array([
    #	[1, 2],
    #	[3, 4],
    #]))
    convoluted = conv(img, filter_sharpen)
    #print(convoluted)
    cv2.imshow('image', convoluted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

 

    return


main()
