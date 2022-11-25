# import modules
import cv2 ,numpy as np

# set the window name
window="Include Help"

# create a blank image
# the image size is (512,512) and 3 layered
image=np.zeros((512,512,3),np.uint8)

# set the name to the window
cv2.namedWindow(window)

# Create the Event Capturing Function
def capture_event(event,x,y,flags,params):
    # event= click of the mouse
    # x,y are position of cursor
    # check the event if it was right click
    if event==cv2.EVENT_RBUTTONDOWN:
        # create a circle at that position
        # of radius 30 and color red
        cv2.circle(image,(x,y),30,(0,0,255),-1)
    # Check if the event was left click
    if event==cv2.EVENT_LBUTTONDBLCLK:
        # create a circle at that position
        # of radius 30 and color greeen
        cv2.circle(image,(x,y),30,(0,255,0),-1)
    #  check if the event was scrolling
    if event==cv2.EVENT_MBUTTONDBLCLK:
        # create a circle at that position
        # of radius 30 and color  blue
        cv2.circle(image,(x,y),30,(255,0,0),-1)

# set the mouse settin function
cv2.setMouseCallback(window,capture_event)

# create a loop untill we press the button
while True:
    cv2.imshow(window,image)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()