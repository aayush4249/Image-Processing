import cv2
import numpy as np
import sys

#Convert Image to Black and White
def binary(image):

    height, width = image.shape
    output = image

    for i in range(height):
        for j in range(width):
            pixel = image[i, j]

            if (pixel < 127):
                output[i, j] = 0
            else:
                output[i, j] = 255

    return output

def count_regions(img):

    print("Start First Pass")

    current = 1

    img = np.array(img)
    labels = np.array(img)

    # Storing label conversions
    conversions = []
    conversions.append([])
    conversions.append([])

    count = 0

    for i in range(1,len(img)):
        for j in range(1,len(img[0])):

            if img[i][j] <255:

                x_label = labels[i][j-1]
                y_label = labels[i-1][j]


                if x_label < 255:
                    
                    # Both x and y are labeled
                    # connect and pick min value
                    if y_label < 255:

                        if not x_label == y_label:
                            
                            labels[i][j] = min(x_label,y_label)

                            if max(x_label,y_label) not in conversions[0]:
                                
                                conversions[0].append(max(x_label,y_label))
                                conversions[1].append(min(x_label,y_label))
                               

                            elif max(x_label,y_label) in conversions[0]:
                                
                                index = conversions[0].index(max(x_label, y_label))

                                if conversions[1][index] > min(x_label,y_label):
                                    
                                    l = conversions[1][index]
                                    conversions[1][index] = min(x_label,y_label)

                                    while l in conversions[0] and count < 100:

                                        count += 1
                                        index = conversions[0].index(l)
                                        l = conversions[1][index]
                                        conversions[1][index] = min(x_label,y_label)
                                    
                                    conversions[0].append(l)
                                    conversions[1].append(min(x_label,y_label))
                        else:

                            labels[i][j] = y_label
                    
                    # Only x coordinate has a label
                    else:

                        labels[i][j] = x_label
                
                # Only y coordinate has a label
                elif y_label < 255:

                    labels[i][j] = y_label

                # neither x nor y has a label
                else:

                    labels[i][j] = current
                    current+= 1

    print("Starting Second Pass")
    count = 1
    for index,value in enumerate(conversions[0]):

        if conversions[1][index] in conversions[0] and count < 100:

            #Use equivalency to correct values
            count += 1
            equivalency = conversions[0].index(conversions[1][index])
            conversions[1][index] = conversions[1][equivalency]
    
    for i in range(1, len(labels)):
        for j in range(1, len(labels[0])):

            if labels[i][j] in conversions[0]:
                index = conversions[0].index(labels[i][j])
                labels[i][j] = conversions[1][index]
                
    return labels

def main():


    np.set_printoptions(threshold=sys.maxsize)
    img = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)
    img2 = (np.array([
        [0, 0, 255, 255, 255], 
        [0, 255, 0, 0, 255], 
        [255, 0, 0, 255, 255], 
        [255, 255, 255, 255, 0], 
        [255, 0, 255, 0, 255]] ))
    

    
    
    out = binary(img)
    out = np.array(img)
    sol = count_regions(out)
    #cv2.imshow('image', sol)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    print(sol)
    


   
    return


main()
