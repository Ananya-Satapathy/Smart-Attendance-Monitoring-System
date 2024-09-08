import cv2

# Initialize the camera
cam_port = 0  # Use 0 for the default camera, or change it to the appropriate port number
cam = cv2.VideoCapture(cam_port)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

# Reading the input person's name
inp = input('Enter person name: ')

# Loop to continuously capture images
while (1):
    result,image = cam.read()
    imshow(inp, image)
    if waitKey(5):
        imwrite(inp+".png", image)
        print("image taken")

# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")

    