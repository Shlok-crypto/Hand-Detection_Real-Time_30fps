import cv2 as cv
import mediapipe as mp
import time

def handtracking():
    capture = cv.VideoCapture(0)

    mphands = mp.solutions.hands
    hands = mphands.Hands()
    mpdraw = mp.solutions.drawing_utils

    preTime = 0
    curTime = 0

    while True:
        _, frame = capture.read()

    #Convert frame into RGB and pass into hands.process()
        frameRGB = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        results = hands.process(frameRGB)

    #Check if any hand discovered
        if results.multi_hand_landmarks:

        #Extract the hands
            for handlms in results.multi_hand_landmarks:

            # getting id, landmarkInfo(x,y) from handlms
                for id, lm in enumerate(handlms.landmark):
                    h, w, c = frame.shape

                # location of the landmarks(x,y) per id(point)
                    cx ,cy, = int(lm.x*w), int(lm.y*h)

                # draw indivitual landmarks
                    # tip of the pointer finger
                    if id == 8:
                        cv.circle(frame,(cx,cy),5,(156,118,237),10)

            # Drawing the landmarks and connections(lines)
                mpdraw.draw_landmarks(frame,handlms, mphands.HAND_CONNECTIONS)

    # Frame rate
        frame = cv.flip(frame, 1)
        curTime = time.time()
        fps = 1 / (curTime - preTime)
        preTime = curTime
        cv.putText(frame,str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),2)


        cv.imshow("image",frame)


        if cv.waitKey(1) == ord('q'):
            break
    capture.release()
    cv.destroyAllWindows()























    # capture = cv.VideoCapture(0)
    #
    # mpHands = mp.solutions.hands
    # hands = mpHands.Hands()
    # mpDraw = mp.solutions.drawing_utils
    #
    # pTime = 0
    # cTime = 0
    #
    # while True:
    #     success, img = capture.read()
    #     imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    #     results = hands.process(imgRGB)
    #     # print(results.multi_hand_landmarks)
    #
    #     if results.multi_hand_landmarks:
    #         for handLms in results.multi_hand_landmarks:
    #             mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    #
    #     cTime = time.time()
    #     fps = 1 / (cTime - pTime)
    #     pTime = cTime
    #
    #     cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
    #     img = cv.flip(img,1)
    #     cv.imshow("Image", img)
    #
    #     if cv.waitKey(45) == ord('q'):
    #         break
    #
    # capture.release()
    # cv.destroyAllWindows()

