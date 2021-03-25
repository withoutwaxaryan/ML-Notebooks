import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./background.jpg')

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv", hsv)

        # how to get hsv value
        # lower : hue - 10, 100, 100 ; higher : hue + 10, 255 ,255
        red = np.uint8([[[0, 0, 255]]]) #bgr value of red
        # black = np.uint8([[0, 0, 0]]])
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        # hsv_black = cv2.cvtColor(black, cv2.COLOR_BGR2HSV)
        #print(hsv_red)
        # print(hsv_black)
    

        #threshold the hsv to get only red colour
        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])
        # l_black = np.array([0, 100, 100])
        # u_black = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, l_red, u_red)
        # mask = cv2.inRange(hsv, l_black, u_black)
        #cv2.imshow("mask", mask)

        part1 = cv2.bitwise_and(back, back, mask=mask)
        #cv2.imshow("part1", part1)

        mask= cv2.bitwise_not(mask)

        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("mask", part2)
        cv2.imshow("cloak", part1 + part2)

        if cv2.waitKey(5) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()