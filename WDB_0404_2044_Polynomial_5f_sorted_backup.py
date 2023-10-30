import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np

### Initialize the Welding Video
cap_w = cv2.VideoCapture('welding/2.mp4')

### Create the ColorFinder object
myColorFinder = ColorFinder(False)

### HSV color of Welding
hsvVals_w = {'hmin': 25, 'smin': 20, 'vmin': 141, 'hmax': 33, 'smax': 255, 'vmax': 255}

### Variables
cnt_center_pos = []

first_frame_pos = []
second_frame_pos = []
third_frame_pos = []
fourth_frame_pos = []
fifth_frame_pos = []

first_frame_pos_sorted = []
second_frame_pos_sorted = []
third_frame_pos_sorted = []
fourth_frame_pos_sorted = []
fifth_frame_pos_sorted = []

upper_5pos = []
lower_5pos = []

upper_x = []
upper_y = []
lower_x = []
lower_y = []

A1 = 0
B1 = 0
C1 = 0
A2 = 0
B2 = 0
C2 = 0

# posListX = []
# posListY = []
# first_up_cnt_center_pos = []
# second_up_cnt_center_pos = []
# third_up_cnt_center_pos = []
# fourth_up_cnt_center_pos = []
# up_first_pos_x = []
# up_first_pos_y = []

xList = [item for item in range(0, 837)]


while True:
    ### Grab the image
    success, img = cap_w.read()
    #img = cv2.imread("Files/Ball.png")
    #img = cv2.imread("welding/scene00029.png")

    ### Crop the Basketball image
    #img = img[0:900, :]
    ### Crop the Welding image
    #img = img[0:520, 0:848]
    #2
    img = img[0:415, 0:837]

    ### Find the Color Welding Spark
    imgColor, mask = myColorFinder.update(img, hsvVals_w)
    ### Find the contours of the Welding Sparks
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        cnt_moment = cv2.moments(cnt)
        center_x = int( cnt_moment['m10'] / cnt_moment['m00'])
        center_y = int( cnt_moment['m01'] / cnt_moment['m00'])
        cnt_center_pos.append([center_x, center_y])

    #print(cnt_center_pos)

    if len(cnt_center_pos) == 10 :
        first_frame_pos = [cnt_center_pos[0], cnt_center_pos[1]]
        second_frame_pos = [cnt_center_pos[2], cnt_center_pos[3]]
        third_frame_pos = [cnt_center_pos[4], cnt_center_pos[5]]
        fourth_frame_pos = [cnt_center_pos[6], cnt_center_pos[7]]
        fifth_frame_pos = [cnt_center_pos[8], cnt_center_pos[9]]

        # print(first_frame_pos)
        # print(second_frame_pos)
        # print(third_frame_pos)
        # print(fourth_frame_pos)
        # print(fifth_frame_pos)

        #sorted reverse=True
        def take_second(elem):
            return elem[1]
        first_frame_pos_sorted = sorted(first_frame_pos, key=take_second, reverse=True)
        second_frame_pos_sorted = sorted(second_frame_pos, key=take_second, reverse=True)
        third_frame_pos_sorted = sorted(third_frame_pos, key=take_second, reverse=True)
        fourth_frame_pos_sorted = sorted(fourth_frame_pos, key=take_second, reverse=True)
        fifth_frame_pos_sorted = sorted(fifth_frame_pos, key=take_second, reverse=True)

        #print(first_frame_pos_sorted)


        upper_5pos = [first_frame_pos_sorted[0], second_frame_pos_sorted[0], third_frame_pos_sorted[0], fourth_frame_pos_sorted[0], fifth_frame_pos_sorted[0]]
        lower_5pos = [first_frame_pos_sorted[1], second_frame_pos_sorted[1], third_frame_pos_sorted[1], fourth_frame_pos_sorted[1], fifth_frame_pos_sorted[1]]


        upper_x = [upper_5pos[0][0], upper_5pos[1][0], upper_5pos[2][0], upper_5pos[3][0], upper_5pos[4][0]]
        upper_y = [upper_5pos[0][1], upper_5pos[1][1], upper_5pos[2][1], upper_5pos[3][1], upper_5pos[4][1]]

        lower_x = [lower_5pos[0][0], lower_5pos[1][0], lower_5pos[2][0], lower_5pos[3][0], lower_5pos[4][0]]
        lower_y = [lower_5pos[0][1], lower_5pos[1][1], lower_5pos[2][1], lower_5pos[3][1], lower_5pos[4][1]]

        # upper_x_np_array = np.array(upper_x)
        # upper_y_np_array = np.array(upper_y)
        # lower_x_np_array = np.array(lower_x)
        # lower_y_np_array = np.array(lower_y)
        print(upper_x)
        print(upper_y)
        print(lower_x)
        print(lower_y)
        A1, B1, C1 = np.polyfit(upper_x, upper_y, 2)
        A2, B2, C2 = np.polyfit(lower_x, lower_y, 2)
        print(A1, B1, C1)
        print(A2, B2, C2)


    else:
        pass

    for x in xList:
        y1 = int(A1 * x ** 2 + B1 * x + C1)
        y2 = int(A2 * x ** 2 + B2 * x + C2)
        print(y1, y2)
        cv2.circle(img, (x, y1), 1, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x, y2), 1, (255, 0, 255), cv2.FILLED)





    # #
    # # A, B, C = np.polyfit(first_up_cnt_center_pos[0][0], first_up_cnt_center_pos[0][1], 2)
    # #
    # # if posListX:
    # #
    # #     ### Polynomial Regression y = Ax^2 + Bx + C
    # #     ### Find the Coefficients
    # #     A, B, C = np.polyfit(posListX, posListY, 2)
    # #
    # #     for x in xList:
    # #         y = int(A*x**2 + B*x + C)
    # #         cv2.circle(imgContours, (x, y), 2, (255, 0, 255), cv2.FILLED)
    # #
    # #
    #
    #
    # ### Display
    # imgContours = cv2.resize(imgContours, (0, 0), None, 0.7, 0.7)
    # ### Display the mask
    # #imgColor = cv2.resize(mask, (0, 0), None, 0.7, 0.7)
    cv2.imshow('Image', img)
    # #cv2.imshow('Image Color', imgColor)
    # cv2.imshow('Image Contours', imgContours)
    #
    # ### waitKey for Ball
    # #cv2.waitKey(50)
    # ### waitKey for Welding
    cv2.waitKey(0)