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

# Function to label the connected regions in an image
# Uses the two pass system
def count_regions(img):

    # First Pass
    print("Starting First Pass")

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

            # Check if pixel is black
            if img[i][j] <255:

                # Check neighbor regions
                x_label = labels[i][j-1]
                y_label = labels[i-1][j]

                # Neighbor above is part of a region
                if x_label < 255:
                    
                    # Neigbor to the side is also part of a region
                    if y_label < 255:

                        # The two pixels aren't part of the same region
                        if not x_label == y_label:
                            
                            # Assign pixel to the region with a lower value
                            labels[i][j] = min(x_label,y_label)

                            # If the greater value isn't in the conversion list
                            if max(x_label,y_label) not in conversions[0]:
                                
                                # Add the values to the conversion list
                                conversions[0].append(max(x_label,y_label))
                                conversions[1].append(min(x_label,y_label))
                               
                            # If the greater value is already part of the conversion list, check if it can be reassigned to a lower region
                            elif max(x_label,y_label) in conversions[0]:
                                
                               
                                index = conversions[0].index(max(x_label, y_label))

                                if conversions[1][index] > min(x_label,y_label):
                                    
                                    l = conversions[1][index]
                                    conversions[1][index] = min(x_label,y_label)

                                    # Depending on the size of the image this can be change to 100
                                    while l in conversions[0] and count < 1000:

                                        count += 1
                                        index = conversions[0].index(l)
                                        l = conversions[1][index]
                                        conversions[1][index] = min(x_label,y_label)
                                    
                                    conversions[0].append(l)
                                    conversions[1].append(min(x_label,y_label))
                        else:

                            labels[i][j] = y_label
                    
                    # Only above neighbor is part of a region
                    else:

                        # Pixel joins the same region as upstairs neighbor
                        labels[i][j] = x_label
                
                # Only neighbor to the side is part of a region
                elif y_label < 255:

                    # Pixel joins the same region as neighbor to the side
                    labels[i][j] = y_label

                # neither x nor y has a label
                else:
                    
                    # New region 
                    labels[i][j] = current
                    current+= 1
    
    # Second pass
    print("Starting Second Pass\n")
    count = 1
    
    # Using the conversion list as an equivalency list
    for index,value in enumerate(conversions[0]):

        if conversions[1][index] in conversions[0] and count < 1000: # Depending on the size of the image this can be change to 100

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

# Function to the the number of black pixels in each region
def get_count(img):


    height, width = img.shape

    count = 0
    components = {} # Dictionary keeps track of number of pixels per region

    # Iterate through image
    for i in range(height):
        for j in range(width):
            
            if img[i,j] != 255:
                
                # If we encounter a new region thats not already in the dictionary
                if img[i,j] not in components:
                    
                    # Reset the counter and add the new region to the dictionary
                    count = 0
                    count +=1
                    components[img[i,j]] = count
                
                # If the region is already in the dictionary
                elif img[i,j] in components:
                    
                    # Update the region pixel count
                    count += 1
                    pixel = img[i,j]
                    components[pixel] = count

    print("There are",len(components),"connected regions\n")

    region = 1
    for x in components:
        print("Region", region , "has", components[x] ,"black pixel(s)")
        region +=1

    return

def main():


    np.set_printoptions(threshold=sys.maxsize)
    img = cv2.imread('Images/test.png', cv2.IMREAD_GRAYSCALE) 
    img2 = (np.array([
        [0, 0, 255, 255, 255], 
        [0, 255, 0, 0, 255], 
        [255, 0, 0, 255, 255], 
        [255, 255, 255, 255, 0], 
        [255, 0, 255, 0, 255]] ))
   
    
    out = binary(img) 
    cv2.imshow("Original Vs. Binary",out)
    cv2.waitKey(0)
    out = np.array(img)
    sol = count_regions(out)
    print(sol)
    print("\nCount: \n")
    get_count(sol)


   
    return


main()
