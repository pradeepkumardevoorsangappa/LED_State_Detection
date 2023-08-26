## CAPTURING AND CALLING THE SAME IMAGE INTO PROGRAM
import cv2
import datetime
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

###### Captures and saves an image ######
# Start the webcam
cap = cv2.VideoCapture(0)
# Read a frame from the webcam
ret, frame = cap.read()
# Get the current time and date
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# Compose the file name
filename = "image_{}.png".format(timestamp)
# Save the frame with a different name each time the program is executed
cv2.imwrite(filename, frame)
# Release the webcam
cap.release()
# Compose the result string
result = "Image saved as {}".format(filename)
# Write the result to a file
with open("result.txt", "w") as f:
    f.write(result)
# Print the result
print(result)

##### Calls the image ####
# Read the result from the file
with open("result.txt", "r") as f:
    result = f.read()
# Extract the file name from the result
filename = result.split()[-1]
# Load the image using OpenCV
img = cv2.imread(filename)
# Display the image
cv2.imshow("Captured Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

def display(img):
    fig=plt.figure(figsize=(12,10))
    ax=fig.add_subplot(111)
    ax.imshow(img)
    
## Green Image
# Convert the image from BGR to HSV color space
hsvg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
imgg1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#display(imgg1)
# Define range of green color in HSV
lower_green = cv2.inRange(hsvg, (29, 100, 100), (65, 255, 255))
upper_green = cv2.inRange(hsvg, (65, 100, 100), (90, 255, 255))
# Merge the mask of lower and upper green
mask = cv2.addWeighted(lower_green, 1, upper_green, 1.0, 0.0)
# Apply the mask to the original image
resg = cv2.bitwise_and(imgg1, imgg1, mask=mask)
resg = cv2.erode(resg,None, iterations = 1)
resg = cv2.dilate(resg,None, iterations = 6)
# Show the original image and the resulting image with red pixels removed
display(resg)
gimgg=cv2.cvtColor(resg, cv2.COLOR_RGB2GRAY)
display(gimgg)
#bimgg=cv2.medianBlur(gimgg,15)
#print(gimgg.dtype)

circlesg = cv2.HoughCircles(gimgg,cv2.HOUGH_GRADIENT,1,20,param1=150,param2=22,minRadius=0,maxRadius=0)
if circlesg is not None:
    circlesg = np.uint16(np.around(circlesg))
    print('No. of Green Leds:',len(circlesg[0,:]))
    for i in circlesg[0, :]:
        center = (i[0], i[1])
        radius = i[2]
        cv2.circle(imgg1, center, radius, (0, 0, 0), 2)
else: print(circlesg)
display(imgg1)