import cv2
import numpy as np
import FeatureVector as fv

#Assignment 7

def main():

    f = open("Vectors.txt","r")
    file_vectors = []
    vectors = []

    #Get vectors from file
    for i in f:
        i = i.lstrip()
        i = i[1:-2]   
        i = i.replace(" ","")
        file_vectors.append(i)
    
    #Convert to floats
    for x in file_vectors:
       vectors.append([float(i) for i in x.split(',')])
    
    img = cv2.imread("Images/6-2.png", cv2.IMREAD_GRAYSCALE)
    img_vector = fv.get_vector(img)
    #img_vector = img_vector.tolist()
    number = recognise(img_vector,vectors)
    print(number)

    return

#Recognise the number
def recognise(img_vector, vectors):

    number = 0, 
    sum = 0
    highest = 10000

    #Use minimum distance method to guess number
    for i in range(10):

        for j in range(9):
            sum+= abs(img_vector[j] - vectors[i][j])

        if sum < highest:
            highest = sum
            number = i

        sum = 0

    return number


main()


