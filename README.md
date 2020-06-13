# Image Processing

This is a simple image processing and pattern recognition library made using python. Each of the files perform a unique action on the image run with the program. The overall objective of this project was to learn about images processing in python and come up with a new image function. The functionality of each of the programs is explained below:


**Convolution**

This program applies various convolution and correlation filters onto an image after converting it to a greyscale image first. Example filters include a sharpen filter, an edge detection filter, a blurring filter. Essentially any filter can be applied as long as it is given in a N x N matrix such that N is odd.

Ex. Inputting the sharpen kernel given below on a picture of a cat returns a sharper more crisp image:

 0 -1  0<br/>
-1  5 -1<br/>
 0 -1  0<br/>
 
![Example of a sharpening convolutuion](https://github.com/aayush4249/Image-Processing/blob/master/Images/Convolution%20Example.jpg)
 

 


**Connected Components**

An important part of AI, Data Mining and Image Processing is identifying different groups of data and this program returns just that. It converts an image into a binary image and from there counts all the connected components. The program will return the number the number of black connected components and give a count of the number of pixels in each connected region.

**Scaling**

Another important image function, scaling images. This program scales an image down by any given factor.

**Feature Vector And Recognise**

These two programs make up a very basic classifier. The feature vector program takes images of numbers 0 - 9 then splits them into 9 squares and then calculates the feature vector of each square by getting the ratio black to white pixels in the image. The recognise program is given an image of a digit from 0 - 9 that's not in the training set and calculates the feature vector of that image. It then compares them to to previously generated feature vectors using the minimum euclidean distance method and picks the number with the lowest value.

**Double Exposure**

After learning about and implementing the various functions this was my own image operation. This program attempts to create a double exposure image by combining two images to simulate a double exposure environment and then uses a 3x3 or 5x5 filter to remove unneccesary noise from the image resulting in a cleaner looking final image.


