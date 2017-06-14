import numpy as np
import cv2
cap = cv2.VideoCapture(0)

while(True):
   
    ret, frame = cap.read()
    
    cv2.rectangle(frame,(350,350),(450,450),(0,255,0),3)
    cv2.rectangle(frame,(350,240),(450,340),(0,255,0),3)
    cv2.rectangle(frame,(460,240),(560,340),(0,255,0),3)
    cv2.rectangle(frame,(460,350),(560,450),(0,255,0),3)

    cv2.imshow('frame', frame)
        
    if cv2.waitKey(1) & 0xFF == ord('f'):
        print "capture front image"
        file = "/Users/davidchiou/desktop/front_image.png"
        cv2.imwrite(file, frame)
        break

while(True):
   
    ret, frame = cap.read()
    
    cv2.rectangle(frame,(350,350),(450,450),(0,255,0),3)
    cv2.rectangle(frame,(350,240),(450,340),(0,255,0),3)
    cv2.rectangle(frame,(460,240),(560,340),(0,255,0),3)
    cv2.rectangle(frame,(460,350),(560,450),(0,255,0),3)


    cv2.imshow('frame', frame)
        
    if cv2.waitKey(1) & 0xFF == ord('u'):
        print "capture up image"
        file = "/Users/davidchiou/desktop/up_image.png"
        cv2.imwrite(file, frame)
        break

while(True):
   
    ret, frame = cap.read()
    
    cv2.rectangle(frame,(350,350),(450,450),(0,255,0),3)
    cv2.rectangle(frame,(350,240),(450,340),(0,255,0),3)
    cv2.rectangle(frame,(460,240),(560,340),(0,255,0),3)
    cv2.rectangle(frame,(460,350),(560,450),(0,255,0),3)


    cv2.imshow('frame', frame)
        
    if cv2.waitKey(1) & 0xFF == ord('d'):
        print "capture down image"
        file = "/Users/davidchiou/desktop/down_image.png"
        cv2.imwrite(file, frame)
        break

while(True):
   
    ret, frame = cap.read()
    
    cv2.rectangle(frame,(350,350),(450,450),(0,255,0),3)
    cv2.rectangle(frame,(350,240),(450,340),(0,255,0),3)
    cv2.rectangle(frame,(460,240),(560,340),(0,255,0),3)
    cv2.rectangle(frame,(460,350),(560,450),(0,255,0),3)


    cv2.imshow('frame', frame)
        
    if cv2.waitKey(1) & 0xFF == ord('r'):
        print "capture right image"
        file = "/Users/davidchiou/desktop/right_image.png"
        cv2.imwrite(file, frame)
        break

while(True):
   
    ret, frame = cap.read()
    
    cv2.rectangle(frame,(350,350),(450,450),(0,255,0),3)
    cv2.rectangle(frame,(350,240),(450,340),(0,255,0),3)
    cv2.rectangle(frame,(460,240),(560,340),(0,255,0),3)
    cv2.rectangle(frame,(460,350),(560,450),(0,255,0),3)


    cv2.imshow('frame', frame)
        
    if cv2.waitKey(1) & 0xFF == ord('l'):
        print "capture left image"
        file = "/Users/davidchiou/desktop/left_image.png"
        cv2.imwrite(file, frame)
        break

while(True):
   
    ret, frame = cap.read()
    
    cv2.rectangle(frame,(350,350),(450,450),(0,255,0),3)
    cv2.rectangle(frame,(350,240),(450,340),(0,255,0),3)
    cv2.rectangle(frame,(460,240),(560,340),(0,255,0),3)
    cv2.rectangle(frame,(460,350),(560,450),(0,255,0),3)


    cv2.imshow('frame', frame)
        
    if cv2.waitKey(1) & 0xFF == ord('b'):
        print "capture back image"
        file = "/Users/davidchiou/desktop/back_image.png"
        cv2.imwrite(file, frame)
        break

#cap.release()
cv2.destroyWindow('frame')

sticks_0 = ['*' for i in range(6)]
sticks_1 = ['*' for i in range(6)]
sticks_2 = ['*' for i in range(6)]
sticks_3 = ['*' for i in range(6)]
sticks_4 = ['*' for i in range(6)]
sticks_5 = ['*' for i in range(6)]
sticks_6 = ['*' for i in range(6)]
sticks_7 = ['*' for i in range(6)]

def color_identify(image):
    img = cv2.imread(image)
    #img = cv2.imread('front_image.png')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([95, 100, 100])
    upper_blue = np.array([135, 255, 255])

    lower_green = np.array([50, 50, 50])
    upper_green = np.array([89, 255, 255])

    frontlower_red = np.array([0, 100, 100]) #[167, 100, 100] dark
    frontupper_red = np.array([10, 255, 255]) #[255, 255, 255]
    backlower_red = np.array([175, 100, 100])
    backupper_red = np.array([180, 255, 255])


    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    lower_purple = np.array([140, 100, 100]) #[140, 100, 100] dark
    upper_purple = np.array([170, 255, 255]) #[168, 255, 255]

    lower_white = np.array([150, 150, 150])
    upper_white = np.array([255, 255, 255])

    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    res_blue = cv2.bitwise_and(img, img, mask = mask_blue)
    res_blue = cv2.GaussianBlur(res_blue, (25, 25), 0)

    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    res_green = cv2.bitwise_and(img, img, mask = mask_green)
    res_green = cv2.GaussianBlur(res_green, (25, 25), 0)

    frontmask_red = cv2.inRange(hsv, frontlower_red, frontupper_red)
    frontres_red = cv2.bitwise_and(img, img, mask = frontmask_red)
    backmask_red = cv2.inRange(hsv, backlower_red, backupper_red)
    backres_red = cv2.bitwise_and(img, img, mask = backmask_red)

    res_red = frontres_red | backres_red
    res_red = cv2.GaussianBlur(res_red, (25, 25), 0)

    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res_yellow = cv2.bitwise_and(img, img, mask = mask_yellow)
    res_yellow = cv2.GaussianBlur(res_yellow, (25, 25), 0)

    mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)
    res_purple = cv2.bitwise_and(img, img, mask = mask_purple)
    res_purple = cv2.GaussianBlur(res_purple, (25, 25), 0)

    mask_white = cv2.inRange(img, lower_white, upper_white)
    res_white = cv2.bitwise_and(img, img, mask = mask_white)
    res_white = cv2.GaussianBlur(res_white, (25, 25), 0)
    #print img[400, 290, :]
    #print img[400, 400, :]
    #print img[510, 400, :]
    #print img[510, 290, :]
    
    if image == "front_image.png":        
        if res_white[290, 400, 2] != 0 or res_white[290, 400, 0] != 0:
           print "piece_5 front white"
           sticks_5[0] = 'W'
        if res_white[400, 400, 2] != 0 or res_white[400, 400, 0] != 0:
           print "piece_1 front white"
           sticks_1[0] = 'W'
        if res_white[289, 510, 2] != 0 or res_white[289, 510, 0] != 0: 
           print "piece_7  front white"
           sticks_7[0] = 'W'
        if res_white[395, 510, 2] != 0 or res_white[395, 510, 0] != 0:
           print "piece_3 front  white"
           sticks_3[0] = 'W'

        if res_yellow[290, 400, 2] != 0:
           print "piece_5 front yellow"
           sticks_5[0] = 'Y'
        if res_yellow[400, 400, 2] != 0:
           print "piece_1 front yellow"
           sticks_1[0] = 'Y'
        if res_yellow[289, 510, 2] != 0: 
           print "piece_7  front yellow"
           sticks_7[0] = 'Y'
        if res_yellow[395, 510, 2] != 0:
           print "piece_3 front  yellow"
           sticks_3[0] = 'Y'

        if res_blue[290, 400, 2] != 0 or res_blue[290, 400, 0] != 0:
           print "piece_5 front blue"
           sticks_5[0] = 'B'
        if res_blue[400, 400, 2] != 0 or res_blue[400, 400, 0] != 0:
           print "piece_1 front blue"
           sticks_1[0] = 'B'
        if res_blue[289, 510, 2] != 0 or res_blue[289, 510, 0] != 0: 
           print "piece_7  front blue"
           sticks_7[0] = 'B'
        if res_blue[395, 510, 2] != 0 or res_blue[395, 510, 0] != 0:
           print "piece_3 front  blue"
           sticks_3[0] = 'B'

        if res_green[290, 400, 2] != 0 or res_green[290, 400, 0] != 0:
           print "piece_5 front green"
           sticks_5[0] = 'G'
        if res_green[400, 400, 2] != 0 or res_green[400, 400, 0] != 0:
           print "piece_1 front green"
           sticks_1[0] = 'G'
        if res_green[289, 510, 2] != 0 or res_green[289, 510, 0] != 0: 
           print "piece_7  front green"
           sticks_7[0] = 'G'
        if res_green[395, 510, 2] != 0 or res_green[395, 510, 0] != 0:
           print "piece_3 front  green"
           sticks_3[0] = 'G'

        if res_red[290, 400, 2] != 0:
           print "piece_5 front red"
           sticks_5[0] = 'R'
        if res_red[400, 400, 2] != 0:
           print "piece_1 front red"
           sticks_1[0] = 'R'
        if res_red[289, 510, 2] != 0: 
           print "piece_7  front red"
           sticks_7[0] = 'R'
        if res_red[395, 510, 2] != 0:
           print "piece_3 front  red"
           sticks_3[0] = 'R'
        
        if res_purple[290, 400, 2] != 0:
           print "piece_5 front orange"
           sticks_5[0] = 'O'
        if res_purple[400, 400, 2] != 0:
           print "piece_1 front orange"
           sticks_1[0] = 'O'
        if res_purple[289, 510, 2] != 0: 
           print "piece_7  front orange"
           sticks_7[0] = 'O'
        if res_purple[395, 510, 2] != 0:
           print "piece_3 front  orange"
           sticks_3[0] = 'O'
    
    elif image == "up_image.png":        
        if res_white[290, 400, 2] != 0 or res_white[290, 400, 0] != 0:
           print "piece_4 up white"
           sticks_4[4] = 'W'
        if res_white[400, 400, 2] != 0 or res_white[400, 400, 0] != 0:
           print "piece_5 up white"
           sticks_5[4] = 'W'
        if res_white[289, 510, 2] != 0 or res_white[289, 510, 0] != 0: 
           print "piece_6  up white"
           sticks_6[4] = 'W'
        if res_white[395, 510, 2] != 0 or res_white[395, 510, 0] != 0:
           print "piece_7 up  white"
           sticks_7[4] = 'W'
        
        if res_yellow[290, 400, 2] != 0:
           print "piece_4 up yellow"
           sticks_4[4] = 'Y'
        if res_yellow[400, 400, 2] != 0:
           print "piece_5 up yellow"
           sticks_5[4] = 'Y'
        if res_yellow[289, 510, 2] != 0: 
           print "piece_6  up yellow"
           sticks_6[4] = 'Y'
        if res_yellow[395, 510, 2] != 0:
           print "piece_7 up  yellow"
           sticks_7[4] = 'Y'

        if res_green[290, 400, 2] != 0 or res_green[290, 400, 0] != 0:
           print "piece_4 up green"
           sticks_4[4] = 'G'
        if res_green[400, 400, 2] != 0 or res_green[400, 400, 0] != 0:
           print "piece_5 up green"
           sticks_5[4] = 'G'
        if res_green[289, 510, 2] != 0 or res_green[289, 510, 0] != 0: 
           print "piece_6  up green"
           sticks_6[4] = 'G'
        if res_green[395, 510, 2] != 0 or res_green[395, 510, 0] != 0:
           print "piece_7 up  green"
           sticks_7[4] = 'G'

        if res_blue[290, 400, 2] != 0 or res_blue[290, 400, 0] != 0:
           print "piece_4 up blue"
           sticks_4[4] = 'B'
        if res_blue[400, 400, 2] != 0 or res_blue[400, 400, 0] != 0:
           print "piece_5 up blue"
           sticks_5[4] = 'B'
        if res_blue[289, 510, 2] != 0 or res_blue[289, 510, 0] != 0: 
           print "piece_6  up blue"
           sticks_6[4] = 'B'
        if res_blue[395, 510, 2] != 0 or res_blue[395, 510, 0] != 0:
           print "piece_7 up  blue"
           sticks_7[4] = 'B'

        if res_red[290, 400, 2] != 0:
           print "piece_4 up red"
           sticks_4[4] = 'R'
        if res_red[400, 400, 2] != 0:
           print "piece_5 up red"
           sticks_5[4] = 'R'
        if res_red[289, 510, 2] != 0: 
           print "piece_6  up red"
           sticks_6[4] = 'R'
        if res_red[395, 510, 2] != 0:
           print "piece_7 up  red"
           sticks_7[4] = 'R'

        if res_purple[290, 400, 2] != 0:
           print "piece_4 up orange"
           sticks_4[4] = 'O'
        if res_purple[400, 400, 2] != 0:
           print "piece_5 up ornage"
           sticks_5[4] = 'O'
        if res_purple[289, 510, 2] != 0: 
           print "piece_6  up orange"
           sticks_6[4] = 'O'
        if res_purple[395, 510, 2] != 0:
           print "piece_7 up  orange"
           sticks_7[4] = 'O'
    
    elif image == "down_image.png":        
        if res_white[290, 400, 2] != 0 or res_white[290, 400, 0] != 0:
           print "piece_1 down white"
           sticks_1[5] = 'W'
        if res_white[400, 400, 2] != 0 or res_white[400, 400, 0] != 0:
           print "piece_0 down white"
           sticks_0[5] = 'W'
        if res_white[289, 510, 2] != 0 or res_white[289, 510, 0] != 0: 
           print "piece_3  down white"
           sticks_3[5] = 'W'
        if res_white[395, 510, 2] != 0 or res_white[395, 510, 0] != 0:
           print "piece_2 down  white"
           sticks_2[5] = 'W'
        
        if res_yellow[290, 400, 2] != 0:
           print "piece_1 down yellow"
           sticks_1[5] = 'Y'
        if res_yellow[400, 400, 2] != 0:
           print "piece_0 down yellow"
           sticks_0[5] = 'Y'
        if res_yellow[289, 510, 2] != 0: 
           print "piece_3  down yellow"
           sticks_3[5] = 'Y'
        if res_yellow[395, 510, 2] != 0:
           print "piece_2 down  yellow"
           sticks_2[5] = 'Y'

        if res_green[290, 400, 2] != 0 or res_green[290, 400, 0] != 0:
           print "piece_1 down green"
           sticks_1[5] = 'G'
        if res_green[400, 400, 2] != 0 or res_green[400, 400, 0] != 0:
           print "piece_0 down green"
           sticks_0[5] = 'G'
        if res_green[289, 510, 2] != 0 or res_green[289, 510, 0] != 0: 
           print "piece_3  down green"
           sticks_3[5] = 'G'
        if res_green[395, 510, 2] != 0 or res_green[395, 510, 0] != 0:
           print "piece_2 down  green"
           sticks_2[5] = 'G'

        if res_blue[290, 400, 2] != 0 or res_blue[290, 400, 0] != 0:
           print "piece_1 down blue"
           sticks_1[5] = 'B'
        if res_blue[400, 400, 2] != 0 or res_blue[400, 400, 0] != 0:
           print "piece_0 down blue"
           sticks_0[5] = 'B'
        if res_blue[289, 510, 2] != 0 or res_blue[289, 510, 0] != 0: 
           print "piece_3  down blue"
           sticks_3[5] = 'B'
        if res_blue[395, 510, 2] != 0 or res_blue[395, 510, 0] != 0:
           print "piece_2 down  blue"
           sticks_2[5] = 'B'

        if res_red[290, 400, 2] != 0:
           print "piece_1 down red"
           sticks_1[5] = 'R'
        if res_red[400, 400, 2] != 0:
           print "piece_0 down red"
           sticks_0[5] = 'R'
        if res_red[289, 510, 2] != 0: 
           print "piece_3  down red"
           sticks_3[5] = 'R'
        if res_red[395, 510, 2] != 0:
           print "piece_2 down  red"
           sticks_2[5] = 'R'

        if res_purple[290, 400, 2] != 0:
           print "piece_1 down orange"
           sticks_1[5] = 'O'
        if res_purple[400, 400, 2] != 0:
           print "piece_0 down ornage"
           sticks_0[5] = 'O'
        if res_purple[289, 510, 2] != 0: 
           print "piece_3  down orange"
           sticks_3[5] = 'O'
        if res_purple[395, 510, 2] != 0:
           print "piece_2 down  orange"
           sticks_2[5] = 'O'

    elif image == "right_image.png":        
        if res_white[290, 400, 2] != 0 or res_white[290, 400, 0] != 0:
           print "piece_7 right white"
           sticks_7[1] = 'W'
        if res_white[400, 400, 2] != 0 or res_white[400, 400, 0] != 0:
           print "piece_3 right white"
           sticks_3[1] = 'W'
        if res_white[289, 510, 2] != 0 or res_white[289, 510, 0] != 0: 
           print "piece_6  right white"
           sticks_6[1] = 'W'
        if res_white[395, 510, 2] != 0 or res_white[395, 510, 0] != 0:
           print "piece_2 right  white"
           sticks_2[1] = 'W'
        
        if res_yellow[290, 400, 2] != 0:
           print "piece_7 right yellow"
           sticks_7[1] = 'Y'
        if res_yellow[400, 400, 2] != 0:
           print "piece_3 right yellow"
           sticks_3[1] = 'Y'
        if res_yellow[289, 510, 2] != 0: 
           print "piece_6  right yellow"
           sticks_6[1] = 'Y'
        if res_yellow[395, 510, 2] != 0:
           print "piece_2 right  yellow"
           sticks_2[1] = 'Y'

        if res_green[290, 400, 2] != 0 or res_green[290, 400, 0] != 0:
           print "piece_7 right green"
           sticks_7[1] = 'G'
        if res_green[400, 400, 2] != 0 or res_green[400, 400, 0] != 0:
           print "piece_3 right green"
           sticks_3[1] = 'G'
        if res_green[289, 510, 2] != 0 or res_green[289, 510, 0] != 0: 
           print "piece_6  right green"
           sticks_6[1] = 'G'
        if res_green[395, 510, 2] != 0 or res_green[395, 510, 0] != 0:
           print "piece_2 right  green"
           sticks_2[1] = 'G'

        if res_blue[290, 400, 2] != 0 or res_blue[290, 400, 0] != 0:
           print "piece_7 right blue"
           sticks_7[1] = 'B'
        if res_blue[400, 400, 2] != 0 or res_blue[400, 400, 0] != 0:
           print "piece_3 right blue"
           sticks_3[1] = 'B'
        if res_blue[289, 510, 2] != 0 or res_blue[289, 510, 0] != 0: 
           print "piece_6  right blue"
           sticks_6[1] = 'B'
        if res_blue[395, 510, 2] != 0 or res_blue[395, 510, 0] != 0:
           print "piece_2 right  blue"
           sticks_2[1] = 'B'

        if res_red[290, 400, 2] != 0:
           print "piece_7 right red"
           sticks_7[1] = 'R'
        if res_red[400, 400, 2] != 0:
           print "piece_3 right red"
           sticks_3[1] = 'R'
        if res_red[289, 510, 2] != 0: 
           print "piece_6  right red"
           sticks_6[1] = 'R'
        if res_red[395, 510, 2] != 0:
           print "piece_2 right  red"
           sticks_2[1] = 'R'

        if res_purple[290, 400, 2] != 0:
           print "piece_7 right orange"
           sticks_7[1] = 'O'
        if res_purple[400, 400, 2] != 0:
           print "piece_3 right ornage"
           sticks_3[1] = 'O'
        if res_purple[289, 510, 2] != 0: 
           print "piece_6  right orange"
           sticks_6[1] = 'O'
        if res_purple[395, 510, 2] != 0:
           print "piece_2 right  orange"
           sticks_2[1] = 'O'

    elif image == "left_image.png":        
        if res_white[290, 400, 2] != 0 or res_white[290, 400, 0] != 0:
           print "piece_4 left white"
           sticks_4[3] = 'W'
        if res_white[400, 400, 2] != 0 or res_white[400, 400, 0] != 0:
           print "piece_0 left white"
           sticks_0[3] = 'W'
        if res_white[289, 510, 2] != 0 or res_white[289, 510, 0] != 0: 
           print "piece_5  left white"
           sticks_5[3] = 'W'
        if res_white[395, 510, 2] != 0 or res_white[395, 510, 0] != 0:
           print "piece_1 left  white"
           sticks_1[3] = 'W'
        
        if res_yellow[290, 400, 2] != 0:
           print "piece_4 left yellow"
           sticks_4[3] = 'Y'
        if res_yellow[400, 400, 2] != 0:
           print "piece_0 left yellow"
           sticks_0[3] = 'Y'
        if res_yellow[289, 510, 2] != 0: 
           print "piece_5  left yellow"
           sticks_5[3] = 'Y'
        if res_yellow[395, 510, 2] != 0:
           print "piece_1 left  yellow"
           sticks_1[3] = 'Y'

        if res_green[290, 400, 2] != 0 or res_green[290, 400, 0] != 0:
           print "piece_4 left green"
           sticks_4[3] = 'G'
        if res_green[400, 400, 2] != 0 or res_green[400, 400, 0] != 0:
           print "piece_0 left green"
           sticks_0[3] = 'G'
        if res_green[289, 510, 2] != 0 or res_green[289, 510, 0] != 0: 
           print "piece_5  left green"
           sticks_5[3] = 'G'
        if res_green[395, 510, 2] != 0 or res_green[395, 510, 0] != 0:
           print "piece_1 left  green"
           sticks_1[3] = 'G'

        if res_blue[290, 400, 2] != 0 or res_blue[290, 400, 0] != 0:
           print "piece_4 left blue"
           sticks_4[3] = 'B'
        if res_blue[400, 400, 2] != 0 or res_blue[400, 400, 0] != 0:
           print "piece_0 left blue"
           sticks_0[3] = 'B'
        if res_blue[289, 510, 2] != 0 or res_blue[289, 510, 0] != 0: 
           print "piece_5  left blue"
           sticks_5[3] = 'B'
        if res_blue[395, 510, 2] != 0 or res_blue[395, 510 ,0] != 0:
           print "piece_1 left  blue"
           sticks_1[3] = 'B'

        if res_red[290, 400, 2] != 0:
           print "piece_4 left red"
           sticks_4[3] = 'R'
        if res_red[400, 400, 2] != 0:
           print "piece_0 left red"
           sticks_0[3] = 'R'
        if res_red[289, 510, 2] != 0: 
           print "piece_5  left red"
           sticks_5[3] = 'R'
        if res_red[395, 510, 2] != 0:
           print "piece_1 left  red"
           sticks_1[3] = 'R'

        if res_purple[290, 400, 2] != 0:
           print "piece_4 left orange"
           sticks_4[3] = 'O'
        if res_purple[400, 400, 2] != 0:
           print "piece_0 left ornage"
           sticks_0[3] = 'O'
        if res_purple[289, 510, 2] != 0: 
           print "piece_5  left orange"
           sticks_5[3] = 'O'
        if res_purple[395, 510, 2] != 0:
           print "piece_1 left  orange"
           sticks_1[3] = 'O'

    elif image == "back_image.png":        
        if res_white[290, 400, 2] != 0 or res_white[290, 400, 0] != 0:
           print "piece_6 back white"
           sticks_6[2] = 'W'
        if res_white[400, 400, 2] != 0 or res_white[400, 400, 0] != 0:
           print "piece_2 back white"
           sticks_2[2] = 'W'
        if res_white[289, 510, 2] != 0 or res_white[289, 510, 0] != 0: 
           print "piece_4  back white"
           sticks_4[2] = 'W'
        if res_white[395, 510, 2] != 0 or res_white[395, 510, 0] != 0:
           print "piece_0 back  white"
           sticks_0[2] = 'W'
        
        if res_yellow[290, 400, 2] != 0:
           print "piece_6 back yellow"
           sticks_6[2] = 'Y'
        if res_yellow[400, 400, 2] != 0:
           print "piece_2 back yellow"
           sticks_2[2] = 'Y'
        if res_yellow[289, 510, 2] != 0: 
           print "piece_4  back yellow"
           sticks_4[2] = 'Y'
        if res_yellow[395, 510, 2] != 0:
           print "piece_0 back  yellow"
           sticks_0[2] = 'Y'

        if res_green[290, 400, 2] != 0 or res_green[290, 400, 0] != 0:
           print "piece_6 back green"
           sticks_6[2] = 'G'
        if res_green[400, 400, 2] != 0 or res_green[400, 400, 0] != 0:
           print "piece_2 back green"
           sticks_2[2] = 'G'
        if res_green[289, 510, 2] != 0 or res_green[289, 510, 0] != 0: 
           print "piece_4  back green"
           sticks_4[2] = 'G'
        if res_green[395, 510, 2] != 0 or res_green[395, 510, 0] != 0:
           print "piece_0 back  green"
           sticks_0[2] = 'G'

        if res_blue[290, 400, 2] != 0 or res_blue[290, 400, 0] != 0:
           print "piece_6 back blue"
           sticks_6[2] = 'B'
        if res_blue[400, 400, 2] != 0 or res_blue[400, 400, 0] != 0:
           print "piece_2 back blue"
           sticks_2[2] = 'B'
        if res_blue[289, 510, 2] != 0 or res_blue[289, 510, 0] != 0: 
           print "piece_4  back blue"
           sticks_4[2] = 'B'
        if res_blue[395, 510, 2] != 0 or res_blue[395, 510, 0] != 0:
           print "piece_0 back  blue"
           sticks_0[2] = 'B'

        if res_red[290, 400, 2] != 0:
           print "piece_6 back red"
           sticks_6[2] = 'R'
        if res_red[400, 400, 2] != 0:
           print "piece_2 back red"
           sticks_2[2] = 'R'
        if res_red[289, 510, 2] != 0: 
           print "piece_4  back red"
           sticks_4[2] = 'R'
        if res_red[395, 510, 2] != 0:
           print "piece_0 back  red"
           sticks_0[2] = 'R'

        if res_purple[290, 400, 2] != 0:
           print "piece_6 back orange"
           sticks_6[2] = 'O'
        if res_purple[400, 400, 2] != 0:
           print "piece_2 back ornage"
           sticks_2[2] = 'O'
        if res_purple[289, 510, 2] != 0: 
           print "piece_4  back orange"
           sticks_4[2] = 'O'
        if res_purple[395, 510, 2] != 0:
           print "piece_0 back  orange"
           sticks_0[2] = 'O'

    """   
    while True:
        cv2.imshow("res_blue", res_blue)
        cv2.imshow("res_green", res_green)
        cv2.imshow("res_white", res_white)
        cv2.imshow("res_yellow", res_yellow)
        cv2.imshow("res_red", res_red)
        cv2.imshow("res_purple", res_purple)
        k = cv2.waitKey(0)
        if k == 27:
            break
    cv2.destroyAllWindows()
    """

images = ['front_image.png', 'up_image.png', 'down_image.png', 'right_image.png', 'left_image.png', 'back_image.png']
for i in images:
    color_identify(i)


from visual import *
# Piece(0) = (0, 0, 0) -> (x, y, z)
# Piece(1) = (1, 0, 0)
# Piece(2) = (0, 1, 0)
# Piece(3) = (1, 1, 0)
# Piece(4) = (0, 0, 1)
# Piece(5) = (1, 0 ,1)
# Piece(6) = (0, 1, 1)
# Piece(7) = (1, 1, 1)

class Piece(object):
    def __init__(self, num, color = None):
        self.num = num
        self.front = color[0]
        self.right = color[1]
        self.back = color[2]
        self.left = color[3]
        self.up = color[4]
        self.down = color[5]
class Cube(object):
    def __init__(self, current_cube):
        self.piece_0 = current_cube[0]
        self.piece_1 = current_cube[1]
        self.piece_2 = current_cube[2]
        self.piece_3 = current_cube[3]
        self.piece_4 = current_cube[4]
        self.piece_5 = current_cube[5]
        self.piece_6 = current_cube[6]
        self.piece_7 = current_cube[7]
    def get_status(self):
        return ' ' * 2 + self.piece_4.back + self.piece_6.back + '\n' + ' ' * 2 + self.piece_0.back + self.piece_2.back + '\n' + self.piece_4.left + self.piece_0.left + self.piece_0.down + self.piece_2.down + self.piece_2.right + self.piece_6.right + self.piece_6.up + self.piece_4.up + '\n' + self.piece_5.left + self.piece_1.left + self.piece_1.down + self.piece_3.down + self.piece_3.right + self.piece_7.right + self.piece_7.up + self.piece_5.up + '\n' + ' ' * 2 + self.piece_1.front + self.piece_3.front + '\n' + ' ' * 2 + self.piece_5.front + self.piece_7.front 

"""
sticks_0 = ['' for i in range(6)]
sticks_1 = ['' for i in range(6)]
sticks_2 = ['' for i in range(6)]
sticks_3 = ['' for i in range(6)]
sticks_4 = ['' for i in range(6)]
sticks_5 = ['' for i in range(6)]
sticks_6 = ['' for i in range(6)]
sticks_7 = ['' for i in range(6)]

print "piece_0:"

sticks_0[2] = raw_input("enter piece_0.back: ")
sticks_0[3] = raw_input("enter piece_0.left: ")
sticks_0[5] = raw_input("enter piece_0.down: ")
print ""

print "piece_1:"

sticks_1[0] = raw_input("enter piece_1.front: ")
sticks_1[3] = raw_input("enter piece_1.left: ")
sticks_1[5] = raw_input("enter piece_1.down: ")
print ""

print "piece_2:"

sticks_2[1] = raw_input("enter piece_2.right: ")
sticks_2[2] = raw_input("enter piece_2.back: ")
sticks_2[5] = raw_input("enter piece_2.down: ")
print ""

print "piece_3:"

sticks_3[0] = raw_input("enter piece_3.front: ")
sticks_3[1] = raw_input("enter piece_3.right: ")
sticks_3[5] = raw_input("enter piece_3.down: ")
print ""

print "piece_4:"

sticks_4[2] = raw_input("enter piece_4.back: ")
sticks_4[3] = raw_input("enter piece_4.left: ")
sticks_4[4] = raw_input("enter piece_4.up: ")
print ""

print "piece_5:"

sticks_5[0] = raw_input("enter piece_5.front: ")
sticks_5[3] = raw_input("enter piece_5.left: ")
sticks_5[4] = raw_input("enter piece_5.up: ")
print ""

print "piece_6:"

sticks_6[1] = raw_input("enter piece_6.right: ")
sticks_6[2] = raw_input("enter piece_6.back: ")
sticks_6[4] = raw_input("enter piece_6.up: ")
print ""

print "piece_7:"

sticks_7[0] = raw_input("enter piece_7.front: ")
sticks_7[1] = raw_input("enter piece_7.right: ")
sticks_7[4] = raw_input("enter piece_7.up: ")
print ""
"""





piece_0 = Piece(0, sticks_0)#Piece(0, ['', '', 'B', 'O', '', 'Y'])
piece_1 = Piece(1, sticks_1)#Piece(1, ['G', '', '', 'O', '', 'Y'])
piece_2 = Piece(2, sticks_2)#Piece(2, ['', 'R', 'B', '', '', 'Y'])
piece_3 = Piece(3, sticks_3)#Piece(3, ['G', 'R', '', '', '', 'Y'])
piece_4 = Piece(4, sticks_4)#Piece(4, ['', '', 'B', 'O', 'W', ''])
piece_5 = Piece(5, sticks_5)#Piece(5, ['G', '', '', 'O', 'W', ''])
piece_6 = Piece(6, sticks_6)#Piece(6, ['', 'R', 'B', '', 'W', ''])
piece_7 = Piece(7, sticks_7)#Piece(7, ['G', 'R', '', '', 'W', ''])

cube_test = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
print cube_test.get_status()

checker = ""

while checker != 'q':
    p_num = raw_input("enter piece num :")
    if p_num == "0":
        position = raw_input("enter position: ")
        fix_color = raw_input("enter color: ")
        if position == 'b':
            cube_test.piece_0.back = fix_color
        elif position == 'l':
            cube_test.piece_0.left = fix_color
        elif position == 'd':
            cube_test.piece_0.down = fix_color
        else:
            print "Invalid!!!"
    elif p_num == "1":
        position = raw_input("enter position: ")
        fix_color = raw_input("enter color: ")
        if position == 'f':
            cube_test.piece_1.front = fix_color
        elif position == 'l':
            cube_test.piece_1.left = fix_color
        elif position == 'd':
            cube_test.piece_1.down = fix_color
        else:
            print "Invalid!!!"
    elif p_num == "2":
        position = raw_input("enter position: ")
        fix_color = raw_input("enter color: ")
        if position == 'r':
            cube_test.piece_2.right = fix_color
        elif position == 'b':
            cube_test.piece_2.back = fix_color
        elif position == 'd':
            cube_test.piece_2.down = fix_color
        else:
            print "Invalid!!!"
    elif p_num == "3":
        position = raw_input("enter position: ")
        fix_color = raw_input("enter color: ")
        if position == 'f':
            cube_test.piece_3.front = fix_color
        elif position == 'r':
            cube_test.piece_3.right = fix_color
        elif position == 'd':
            cube_test.piece_3.down = fix_color
        else:
            print "Invalid!!!"
    elif p_num == "4":
        position = raw_input("enter position: ")
        fix_color = raw_input("enter color: ")
        if position == 'b':
            cube_test.piece_4.back = fix_color
        elif position == 'l':
            cube_test.piece_4.left = fix_color
        elif position == 'u':
            cube_test.piece_4.up = fix_color
        else:
            print "Invalid!!!"

    elif p_num == "5":
        position = raw_input("enter position: ")
        fix_color = raw_input("enter color: ")
        if position == 'f':
            cube_test.piece_5.front = fix_color
        elif position == 'l':
            cube_test.piece_5.left = fix_color
        elif position == 'u':
            cube_test.piece_5.up = fix_color
        else:
            print "Invalid!!!"
    elif p_num == "6":
        position = raw_input("enter position: ")
        fix_color = raw_input("enter color: ")
        if position == 'b':
            cube_test.piece_6.back = fix_color
        elif position == 'r':
            cube_test.piece_6.right = fix_color
        elif position == 'u':
            cube_test.piece_6.up = fix_color
        else:
            print "Invalid!!!"
    elif p_num == "7":
        position = raw_input("enter position: ")
        fix_color = raw_input("enter color: ")
        if position == 'f':
            cube_test.piece_7.front = fix_color
        elif position == 'r':
            cube_test.piece_7.right = fix_color
        elif position == 'u':
            cube_test.piece_7.up = fix_color
        else:
            print "Invalid!!!"
    else:
        print "Lucky~"
    print cube_test.get_status()

    checker = raw_input("enter q to exit: ")







def r_turn(cube):
    #print 'turn the right face'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # right turn will influence piece_2, piece_3, piece_6, piece_7

    # piece_2 case:
    turned_cube.piece_2.front = ''
    turned_cube.piece_2.up = ''
    turned_cube.piece_2.left = ''
    turned_cube.piece_2.right = cube.piece_6.right
    turned_cube.piece_2.down = cube.piece_6.back
    turned_cube.piece_2.back = cube.piece_6.up
    
    # piece_3 case:
    turned_cube.piece_3.up = ''
    turned_cube.piece_3.left = ''
    turned_cube.piece_3.back = ''
    turned_cube.piece_3.right = cube.piece_2.right
    turned_cube.piece_3.down = cube.piece_2.back
    turned_cube.piece_3.front = cube.piece_2.down

    # piece_6 case:
    turned_cube.piece_6.front = ''
    turned_cube.piece_6.left = ''
    turned_cube.piece_6.down = ''
    turned_cube.piece_6.right = cube.piece_7.right
    turned_cube.piece_6.back = cube.piece_7.up
    turned_cube.piece_6.up = cube.piece_7.front

    # piece_7 case:
    turned_cube.piece_7.left = ''
    turned_cube.piece_7.back = ''
    turned_cube.piece_7.down = ''
    turned_cube.piece_7.right = cube.piece_3.right
    turned_cube.piece_7.front = cube.piece_3.down
    turned_cube.piece_7.up = cube.piece_3.front
    
    # others:
    turned_cube.piece_0 = cube.piece_0
    turned_cube.piece_1 = cube.piece_1
    turned_cube.piece_4 = cube.piece_4
    turned_cube.piece_5 = cube.piece_5
    return turned_cube

def l_turn(cube):
    #print 'turn the left face'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # left turn will influence piece_0, piece_1, piece_4, piece_5

    # piece_0 case:
    turned_cube.piece_0.up = ''
    turned_cube.piece_0.front = ''
    turned_cube.piece_0.right = ''
    turned_cube.piece_0.left = cube.piece_1.left
    turned_cube.piece_0.down = cube.piece_1.front
    turned_cube.piece_0.back = cube.piece_1.down

    # piece_1 case:
    turned_cube.piece_1.up = ''
    turned_cube.piece_1.right = ''
    turned_cube.piece_1.back = ''
    turned_cube.piece_1.left = cube.piece_5.left
    turned_cube.piece_1.down = cube.piece_5.front
    turned_cube.piece_1.front = cube.piece_5.up

    # piece_4 case:
    turned_cube.piece_4.right = ''
    turned_cube.piece_4.front = ''
    turned_cube.piece_4.down = ''
    turned_cube.piece_4.left = cube.piece_0.left
    turned_cube.piece_4.back = cube.piece_0.down
    turned_cube.piece_4.up = cube.piece_0.back

    # piece_5 case:
    turned_cube.piece_5.right = ''
    turned_cube.piece_5.back = ''
    turned_cube.piece_5.down = ''
    turned_cube.piece_5.left = cube.piece_4.left
    turned_cube.piece_5.front = cube.piece_4.up
    turned_cube.piece_5.up = cube.piece_4.back

    # others:
    turned_cube.piece_2 = cube.piece_2
    turned_cube.piece_3 = cube.piece_3
    turned_cube.piece_6 = cube.piece_6
    turned_cube.piece_7 = cube.piece_7
    return turned_cube

def u_turn(cube):
    #print 'turn the up face'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # up turn will influence piece_4, piece_5, piece_6, piece_7

    # piece_4 case:
    turned_cube.piece_4.right = ''
    turned_cube.piece_4.front = ''
    turned_cube.piece_4.down = ''
    turned_cube.piece_4.up = cube.piece_5.up
    turned_cube.piece_4.left = cube.piece_5.front
    turned_cube.piece_4.back = cube.piece_5.left

    # piece_5 case:
    turned_cube.piece_5.back = ''
    turned_cube.piece_5.right = ''
    turned_cube.piece_5.down = ''
    turned_cube.piece_5.up = cube.piece_7.up
    turned_cube.piece_5.front = cube.piece_7.right
    turned_cube.piece_5.left = cube.piece_7.front

    # piece_6 case:
    turned_cube.piece_6.left = ''
    turned_cube.piece_6.front = ''
    turned_cube.piece_6.down = ''
    turned_cube.piece_6.up = cube.piece_4.up
    turned_cube.piece_6.back = cube.piece_4.left
    turned_cube.piece_6.right = cube.piece_4.back

    # piece_7 case:
    turned_cube.piece_7.left = ''
    turned_cube.piece_7.back = ''
    turned_cube.piece_7.down = ''
    turned_cube.piece_7.up = cube.piece_6.up
    turned_cube.piece_7.right = cube.piece_6.back
    turned_cube.piece_7.front = cube.piece_6.right

    # others:
    turned_cube.piece_0 = cube.piece_0
    turned_cube.piece_1 = cube.piece_1
    turned_cube.piece_2 = cube.piece_2
    turned_cube.piece_3 = cube.piece_3
    return turned_cube

def d_turn(cube):
    #print 'turn the down face'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # down turn will influence piece_0, piece_1, piece_2, piece_3

    # piece_0 case:
    turned_cube.piece_0.right = ''
    turned_cube.piece_0.front = ''
    turned_cube.piece_0.up = ''
    turned_cube.piece_0.down = cube.piece_2.down
    turned_cube.piece_0.back = cube.piece_2.right
    turned_cube.piece_0.left = cube.piece_2.back

    # piece_1 case:
    turned_cube.piece_1.back = ''
    turned_cube.piece_1.right = ''
    turned_cube.piece_1.up = ''
    turned_cube.piece_1.down = cube.piece_0.down
    turned_cube.piece_1.left = cube.piece_0.back
    turned_cube.piece_1.front = cube.piece_0.left

    # piece_2 case:
    turned_cube.piece_2.left = ''
    turned_cube.piece_2.up = ''
    turned_cube.piece_2.front = ''
    turned_cube.piece_2.down = cube.piece_3.down
    turned_cube.piece_2.back = cube.piece_3.right
    turned_cube.piece_2.right = cube.piece_3.front

    # piece_3 case:
    turned_cube.piece_3.up = ''
    turned_cube.piece_3.left = ''
    turned_cube.piece_3.back = ''
    turned_cube.piece_3.down = cube.piece_1.down
    turned_cube.piece_3.right = cube.piece_1.front
    turned_cube.piece_3.front = cube.piece_1.left

    # others:
    turned_cube.piece_4 = cube.piece_4
    turned_cube.piece_5 = cube.piece_5
    turned_cube.piece_6 = cube.piece_6
    turned_cube.piece_7 = cube.piece_7
    return turned_cube

def f_turn(cube):
    #print 'turn the front face'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # front turn will influence piece_1, piece_3, piece_5, piece_7

    # piece_1 case:
    turned_cube.piece_1.right = ''
    turned_cube.piece_1.back = ''
    turned_cube.piece_1.up = ''
    turned_cube.piece_1.front = cube.piece_3.front
    turned_cube.piece_1.down = cube.piece_3.right
    turned_cube.piece_1.left = cube.piece_3.down

    # piece_3 case:
    turned_cube.piece_3.back = ''
    turned_cube.piece_3.left = ''
    turned_cube.piece_3.up = ''
    turned_cube.piece_3.front = cube.piece_7.front
    turned_cube.piece_3.right = cube.piece_7.up
    turned_cube.piece_3.down = cube.piece_7.right

    # piece_5 case:
    turned_cube.piece_5.right = ''
    turned_cube.piece_5.back = ''
    turned_cube.piece_5.down = ''
    turned_cube.piece_5.front = cube.piece_1.front
    turned_cube.piece_5.up = cube.piece_1.left
    turned_cube.piece_5.left = cube.piece_1.down

    # piece_7 case:
    turned_cube.piece_7.down = ''
    turned_cube.piece_7.left = ''
    turned_cube.piece_7.back = ''
    turned_cube.piece_7.front = cube.piece_5.front
    turned_cube.piece_7.right = cube.piece_5.up
    turned_cube.piece_7.up = cube.piece_5.left

    # others:
    turned_cube.piece_0 = cube.piece_0
    turned_cube.piece_2 = cube.piece_2
    turned_cube.piece_4 = cube.piece_4
    turned_cube.piece_6 = cube.piece_6
    return turned_cube

def b_turn(cube):
    #print 'turn the back face'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # back turn will influence piece_0, piece_2, piece_4, piece_6

    # piece_0 case:
    turned_cube.piece_0.right = ''
    turned_cube.piece_0.front = ''
    turned_cube.piece_0.up = ''
    turned_cube.piece_0.back = cube.piece_4.back
    turned_cube.piece_0.left = cube.piece_4.up
    turned_cube.piece_0.down = cube.piece_4.left

    # piece_2 case:
    turned_cube.piece_2.left = ''
    turned_cube.piece_2.up = ''
    turned_cube.piece_2.front = ''
    turned_cube.piece_2.back = cube.piece_0.back
    turned_cube.piece_2.down = cube.piece_0.left
    turned_cube.piece_2.right = cube.piece_0.down

    # piece_4 case:
    turned_cube.piece_4.front = ''
    turned_cube.piece_4.down = ''
    turned_cube.piece_4.right = ''
    turned_cube.piece_4.back = cube.piece_6.back
    turned_cube.piece_4.up = cube.piece_6.right
    turned_cube.piece_4.left = cube.piece_6.up

    # piece_6 case:
    turned_cube.piece_6.left = ''
    turned_cube.piece_6.down = ''
    turned_cube.piece_6.front = ''
    turned_cube.piece_6.back = cube.piece_2.back
    turned_cube.piece_6.right = cube.piece_2.down
    turned_cube.piece_6.up = cube.piece_2.right

    # others:
    turned_cube.piece_1 = cube.piece_1
    turned_cube.piece_3 = cube.piece_3
    turned_cube.piece_5 = cube.piece_5
    turned_cube.piece_7 = cube.piece_7
    return turned_cube

def r_inverse_turn(cube):
    #print 'turn the right face inversely'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # right turn will influence piece_2, piece_3, piece_6, piece_7

    # piece_2 case:
    turned_cube.piece_2.front = ''
    turned_cube.piece_2.up = ''
    turned_cube.piece_2.left = ''
    turned_cube.piece_2.right = cube.piece_3.right
    turned_cube.piece_2.down = cube.piece_3.front
    turned_cube.piece_2.back = cube.piece_3.down
    
    # piece_3 case:
    turned_cube.piece_3.up = ''
    turned_cube.piece_3.left = ''
    turned_cube.piece_3.back = ''
    turned_cube.piece_3.right = cube.piece_7.right
    turned_cube.piece_3.down = cube.piece_7.front
    turned_cube.piece_3.front = cube.piece_7.up

    # piece_6 case:
    turned_cube.piece_6.front = ''
    turned_cube.piece_6.left = ''
    turned_cube.piece_6.down = ''
    turned_cube.piece_6.right = cube.piece_2.right
    turned_cube.piece_6.back = cube.piece_2.down
    turned_cube.piece_6.up = cube.piece_2.back

    # piece_7 case:
    turned_cube.piece_7.left = ''
    turned_cube.piece_7.back = ''
    turned_cube.piece_7.down = ''
    turned_cube.piece_7.right = cube.piece_6.right
    turned_cube.piece_7.front = cube.piece_6.up
    turned_cube.piece_7.up = cube.piece_6.back
    
    # others:
    turned_cube.piece_0 = cube.piece_0
    turned_cube.piece_1 = cube.piece_1
    turned_cube.piece_4 = cube.piece_4
    turned_cube.piece_5 = cube.piece_5
    return turned_cube

def l_inverse_turn(cube):
    #print 'turn the left face inversely'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # left turn will influence piece_0, piece_1, piece_4, piece_5

    # piece_0 case:
    turned_cube.piece_0.up = ''
    turned_cube.piece_0.front = ''
    turned_cube.piece_0.right = ''
    turned_cube.piece_0.left = cube.piece_4.left
    turned_cube.piece_0.down = cube.piece_4.back
    turned_cube.piece_0.back = cube.piece_4.up

    # piece_1 case:
    turned_cube.piece_1.up = ''
    turned_cube.piece_1.right = ''
    turned_cube.piece_1.back = ''
    turned_cube.piece_1.left = cube.piece_0.left
    turned_cube.piece_1.down = cube.piece_0.back
    turned_cube.piece_1.front = cube.piece_0.down

    # piece_4 case:
    turned_cube.piece_4.right = ''
    turned_cube.piece_4.front = ''
    turned_cube.piece_4.down = ''
    turned_cube.piece_4.left = cube.piece_5.left
    turned_cube.piece_4.back = cube.piece_5.up
    turned_cube.piece_4.up = cube.piece_5.front

    # piece_5 case:
    turned_cube.piece_5.right = ''
    turned_cube.piece_5.back = ''
    turned_cube.piece_5.down = ''
    turned_cube.piece_5.left = cube.piece_1.left
    turned_cube.piece_5.front = cube.piece_1.down
    turned_cube.piece_5.up = cube.piece_1.front

    # others:
    turned_cube.piece_2 = cube.piece_2
    turned_cube.piece_3 = cube.piece_3
    turned_cube.piece_6 = cube.piece_6
    turned_cube.piece_7 = cube.piece_7
    return turned_cube

def u_inverse_turn(cube):
    #print 'turn the up face inversely'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # up turn will influence piece_4, piece_5, piece_6, piece_7

    # piece_4 case:
    turned_cube.piece_4.right = ''
    turned_cube.piece_4.front = ''
    turned_cube.piece_4.down = ''
    turned_cube.piece_4.up = cube.piece_6.up
    turned_cube.piece_4.left = cube.piece_6.back
    turned_cube.piece_4.back = cube.piece_6.right

    # piece_5 case:
    turned_cube.piece_5.back = ''
    turned_cube.piece_5.right = ''
    turned_cube.piece_5.down = ''
    turned_cube.piece_5.up = cube.piece_4.up
    turned_cube.piece_5.front = cube.piece_4.left
    turned_cube.piece_5.left = cube.piece_4.back

    # piece_6 case:
    turned_cube.piece_6.left = ''
    turned_cube.piece_6.front = ''
    turned_cube.piece_6.down = ''
    turned_cube.piece_6.up = cube.piece_7.up
    turned_cube.piece_6.back = cube.piece_7.right
    turned_cube.piece_6.right = cube.piece_7.front

    # piece_7 case:
    turned_cube.piece_7.left = ''
    turned_cube.piece_7.back = ''
    turned_cube.piece_7.down = ''
    turned_cube.piece_7.up = cube.piece_5.up
    turned_cube.piece_7.right = cube.piece_5.front
    turned_cube.piece_7.front = cube.piece_5.left

    # others:
    turned_cube.piece_0 = cube.piece_0
    turned_cube.piece_1 = cube.piece_1
    turned_cube.piece_2 = cube.piece_2
    turned_cube.piece_3 = cube.piece_3
    return turned_cube

def d_inverse_turn(cube):
    #print 'turn the down face inversely'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # down turn will influence piece_0, piece_1, piece_2, piece_3

    # piece_0 case:
    turned_cube.piece_0.right = ''
    turned_cube.piece_0.front = ''
    turned_cube.piece_0.up = ''
    turned_cube.piece_0.down = cube.piece_1.down
    turned_cube.piece_0.back = cube.piece_1.left
    turned_cube.piece_0.left = cube.piece_1.front

    # piece_1 case:
    turned_cube.piece_1.back = ''
    turned_cube.piece_1.right = ''
    turned_cube.piece_1.up = ''
    turned_cube.piece_1.down = cube.piece_3.down
    turned_cube.piece_1.left = cube.piece_3.front
    turned_cube.piece_1.front = cube.piece_3.right

    # piece_2 case:
    turned_cube.piece_2.left = ''
    turned_cube.piece_2.up = ''
    turned_cube.piece_2.front = ''
    turned_cube.piece_2.down = cube.piece_0.down
    turned_cube.piece_2.back = cube.piece_0.left
    turned_cube.piece_2.right = cube.piece_0.back

    # piece_3 case:
    turned_cube.piece_3.up = ''
    turned_cube.piece_3.left = ''
    turned_cube.piece_3.back = ''
    turned_cube.piece_3.down = cube.piece_2.down
    turned_cube.piece_3.right = cube.piece_2.back
    turned_cube.piece_3.front = cube.piece_2.right

    # others:
    turned_cube.piece_4 = cube.piece_4
    turned_cube.piece_5 = cube.piece_5
    turned_cube.piece_6 = cube.piece_6
    turned_cube.piece_7 = cube.piece_7
    return turned_cube

def f_inverse_turn(cube):
    #print 'turn the front face inversely'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # front turn will influence piece_1, piece_3, piece_5, piece_7

    # piece_1 case:
    turned_cube.piece_1.right = ''
    turned_cube.piece_1.back = ''
    turned_cube.piece_1.up = ''
    turned_cube.piece_1.front = cube.piece_5.front
    turned_cube.piece_1.down = cube.piece_5.left
    turned_cube.piece_1.left = cube.piece_5.up

    # piece_3 case:
    turned_cube.piece_3.back = ''
    turned_cube.piece_3.left = ''
    turned_cube.piece_3.up = ''
    turned_cube.piece_3.front = cube.piece_1.front
    turned_cube.piece_3.right = cube.piece_1.down
    turned_cube.piece_3.down = cube.piece_1.left

    # piece_5 case:
    turned_cube.piece_5.right = ''
    turned_cube.piece_5.back = ''
    turned_cube.piece_5.down = ''
    turned_cube.piece_5.front = cube.piece_7.front
    turned_cube.piece_5.up = cube.piece_7.right
    turned_cube.piece_5.left = cube.piece_7.up

    # piece_7 case:
    turned_cube.piece_7.down = ''
    turned_cube.piece_7.left = ''
    turned_cube.piece_7.back = ''
    turned_cube.piece_7.front = cube.piece_3.front
    turned_cube.piece_7.right = cube.piece_3.down
    turned_cube.piece_7.up = cube.piece_3.right

    # others:
    turned_cube.piece_0 = cube.piece_0
    turned_cube.piece_2 = cube.piece_2
    turned_cube.piece_4 = cube.piece_4
    turned_cube.piece_6 = cube.piece_6
    return turned_cube

def b_inverse_turn(cube):
    #print 'turn the back face inversely'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # back turn will influence piece_0, piece_2, piece_4, piece_6

    # piece_0 case:
    turned_cube.piece_0.right = ''
    turned_cube.piece_0.front = ''
    turned_cube.piece_0.up = ''
    turned_cube.piece_0.back = cube.piece_2.back
    turned_cube.piece_0.left = cube.piece_2.down
    turned_cube.piece_0.down = cube.piece_2.right

    # piece_2 case:
    turned_cube.piece_2.left = ''
    turned_cube.piece_2.up = ''
    turned_cube.piece_2.front = ''
    turned_cube.piece_2.back = cube.piece_6.back
    turned_cube.piece_2.down = cube.piece_6.right
    turned_cube.piece_2.right = cube.piece_6.up

    # piece_4 case:
    turned_cube.piece_4.front = ''
    turned_cube.piece_4.down = ''
    turned_cube.piece_4.right = ''
    turned_cube.piece_4.back = cube.piece_0.back
    turned_cube.piece_4.up = cube.piece_0.left
    turned_cube.piece_4.left = cube.piece_0.down

    # piece_6 case:
    turned_cube.piece_6.left = ''
    turned_cube.piece_6.down = ''
    turned_cube.piece_6.front = ''
    turned_cube.piece_6.back = cube.piece_4.back
    turned_cube.piece_6.right = cube.piece_4.up
    turned_cube.piece_6.up = cube.piece_4.left

    # others:
    turned_cube.piece_1 = cube.piece_1
    turned_cube.piece_3 = cube.piece_3
    turned_cube.piece_5 = cube.piece_5
    turned_cube.piece_7 = cube.piece_7
    return turned_cube

def double_r_turn(cube):
    turned_cube = r_turn(cube)
    turned_cube = r_turn(turned_cube)
    return turned_cube

def double_u_turn(cube):
    turned_cube = u_turn(cube)
    turned_cube = u_turn(turned_cube)
    return turned_cube

def double_f_turn(cube):
    turned_cube = f_turn(cube)
    turned_cube = f_turn(turned_cube)
    return turned_cube

# f r b l u d

color_pair = {'B': 'G', 'G': 'B', 'O': 'R', 'R': 'O', 'W': 'Y', 'Y': 'W'}
piece0_sticks = ['*', '*', cube_test.piece_0.back , cube_test.piece_0.left, '*', cube_test.piece_0.down]
piece1_sticks = [color_pair[cube_test.piece_0.back], '*', '*', cube_test.piece_0.left, '*', cube_test.piece_0.down]
piece2_sticks = ['*', color_pair[cube_test.piece_0.left], cube_test.piece_0.back, '*', '*', cube_test.piece_0.down]
piece3_sticks = [color_pair[cube_test.piece_0.back], color_pair[cube_test.piece_0.left], '*', '*', '*', cube_test.piece_0.down]
piece4_sticks = ['*', '*', cube_test.piece_0.back, cube_test.piece_0.left, color_pair[cube_test.piece_0.down], '*']
piece5_sticks = [color_pair[cube_test.piece_0.back], '*', '*', cube_test.piece_0.left, color_pair[cube_test.piece_0.down], '*']
piece6_sticks = ['*', color_pair[cube_test.piece_0.left], cube_test.piece_0.back, '*', color_pair[cube_test.piece_0.down], '*']
piece7_sticks = [color_pair[cube_test.piece_0.back], color_pair[cube_test.piece_0.left], '*', '*', color_pair[cube_test.piece_0.down], '*']

solved_piece_0 = Piece(0, piece0_sticks)
solved_piece_1 = Piece(1, piece1_sticks)
solved_piece_2 = Piece(2, piece2_sticks)
solved_piece_3 = Piece(3, piece3_sticks)
solved_piece_4 = Piece(4, piece4_sticks)
solved_piece_5 = Piece(5, piece5_sticks)
solved_piece_6 = Piece(6, piece6_sticks)
solved_piece_7 = Piece(7, piece7_sticks)

solved_cube = Cube([solved_piece_0, solved_piece_1, solved_piece_2, solved_piece_3, solved_piece_4, solved_piece_5, solved_piece_6, solved_piece_7])

print solved_cube.get_status()

def cube_search():
    frontier_unsolved = [[0, [], cube_test]]
    visited_unsolved = []
    dict_unsolved = {}

    frontier_solved = [[0, [], solved_cube]]
    visited_solved = []
    dict_solved = {}

    for i in range(6):
        
        time1 = len(frontier_unsolved)
        time2 = len(frontier_solved)
        for j in range(time1):
            curcost, curpath, curstatus = frontier_unsolved.pop()
            if curstatus.get_status() not in visited_unsolved:
                visited_unsolved.append(curstatus.get_status())
                dict_unsolved[curstatus.get_status()] = curpath

                for status in dict_unsolved:
                    if status in dict_solved:
                        return dict_unsolved[status] + dict_solved[status][::-1]
                        #exit()
            
                r_turned = r_turn(curstatus)
                frontier_unsolved.append([curcost + 1, curpath + ['r'], r_turned])
                
                #l_turned = l_turn(curstatus)
                #frontier_unsolved.append([curcost + 1, curpath + ['l'], l_turned])

                u_turned = u_turn(curstatus)
                frontier_unsolved.append([curcost + 1, curpath + ['u'], u_turned])

                #d_turned = d_turn(curstatus)
                #frontier_unsolved.append([curcost + 1, curpath + ['d'], d_turned])

                f_turned = f_turn(curstatus)
                frontier_unsolved.append([curcost + 1, curpath + ['f'], f_turned])

                #b_turned = b_turn(curstatus)
                #frontier_unsolved.append([curcost + 1, curpath + ['b'], b_turned])

                r_inverse_turned = r_inverse_turn(curstatus)
                frontier_unsolved.append([curcost + 1, curpath + ['r_'], r_inverse_turned])

                #l_inverse_turned = l_inverse_turn(curstatus)
                #frontier_unsolved.append([curcost + 1, curpath + ['l_'], l_inverse_turned])

                u_inverse_turned = u_inverse_turn(curstatus)
                frontier_unsolved.append([curcost + 1, curpath + ['u_'], u_inverse_turned])

                #d_inverse_turned = d_inverse_turn(curstatus)
                #frontier_unsolved.append([curcost + 1, curpath + ['d_'], d_inverse_turned])

                f_inverse_turned = f_inverse_turn(curstatus)
                frontier_unsolved.append([curcost + 1, curpath + ['f_'], f_inverse_turned])

                #b_inverse_turned = b_inverse_turn(curstatus)
                #frontier_unsolved.append([curcost + 1, curpath + ['b_'], b_inverse_turned])
                
                f_double_turned = double_f_turn(curstatus)
                frontier_unsolved.append([curcost + 1, curpath + ['f2'], f_double_turned])

                r_double_turned = double_r_turn(curstatus)
                frontier_unsolved.append([curcost + 1, curpath + ['r2'], r_double_turned])

                u_double_turned = double_u_turn(curstatus)
                frontier_unsolved.append([curcost + 1, curpath + ['u2'], u_double_turned])
                
                frontier_unsolved.sort()
                frontier_unsolved.reverse()

        for k in range(time2):
            curcost, curpath, curstatus = frontier_solved.pop()
            if curstatus.get_status() not in visited_solved:
                visited_solved.append(curstatus.get_status())
                dict_solved[curstatus.get_status()] = curpath

                for status in dict_solved:
                    if status in dict_unsolved:
                        return dict_unsolved[status] + dict_solved[status][::-1]
                        #exit()
                    
                r_turned = r_turn(curstatus)
                frontier_solved.append([curcost + 1, curpath + ['r_'], r_turned])

                #l_turned = l_turn(curstatus)
                #frontier_solved.append([curcost + 1, curpath + ['l_'], l_turned])

                u_turned = u_turn(curstatus)
                frontier_solved.append([curcost + 1, curpath + ['u_'], u_turned])

                #d_turned = d_turn(curstatus)
                #frontier_solved.append([curcost + 1, curpath + ['d_'], d_turned])

                f_turned = f_turn(curstatus)
                frontier_solved.append([curcost + 1, curpath + ['f_'], f_turned])

                #b_turned = b_turn(curstatus)
                #frontier_solved.append([curcost + 1, curpath + ['b_'], b_turned])

                r_inverse_turned = r_inverse_turn(curstatus)
                frontier_solved.append([curcost + 1, curpath + ['r'], r_inverse_turned])

                #l_inverse_turned = l_inverse_turn(curstatus)
                #frontier_solved.append([curcost + 1, curpath + ['l'], l_inverse_turned])

                u_inverse_turned = u_inverse_turn(curstatus)
                frontier_solved.append([curcost + 1, curpath + ['u'], u_inverse_turned])

                #d_inverse_turned = d_inverse_turn(curstatus)
                #frontier_solved.append([curcost + 1, curpath + ['d'], d_inverse_turned])

                f_inverse_turned = f_inverse_turn(curstatus)
                frontier_solved.append([curcost + 1, curpath + ['f'], f_inverse_turned])

                #b_inverse_turned = b_inverse_turn(curstatus)
                #frontier_solved.append([curcost + 1, curpath + ['b'], b_inverse_turned])

               
                f_double_turned = double_f_turn(curstatus)
                frontier_solved.append([curcost + 1, curpath + ['f2'], f_double_turned])

                r_double_turned = double_r_turn(curstatus)
                frontier_solved.append([curcost + 1, curpath + ['r2'], r_double_turned])

                u_double_turned = double_u_turn(curstatus)
                frontier_solved.append([curcost + 1, curpath + ['u2'], u_double_turned])

                frontier_solved.sort()
                frontier_solved.reverse()

steps = cube_search()
print steps

color_trans = {'R': color.red, 'O': color.orange, 'G': color.green, 'B': color.blue, 'W': color.white, 'Y': color.yellow}


fps = 48

faces = {
            'r': ([color_trans[cube_test.piece_7.right], color_trans[cube_test.piece_6.right], color_trans[cube_test.piece_3.right], color_trans[cube_test.piece_2.right]], (1, 0, 0)), 
            'l': ([color_trans[cube_test.piece_1.left], color_trans[cube_test.piece_0.left], color_trans[cube_test.piece_5.left], color_trans[cube_test.piece_4.left]], (-1, 0, 0)),  
            'b': ([color_trans[cube_test.piece_4.back], color_trans[cube_test.piece_0.back], color_trans[cube_test.piece_6.back], color_trans[cube_test.piece_2.back]], (0, 1, 0)),
            'f': ([color_trans[cube_test.piece_1.front], color_trans[cube_test.piece_5.front], color_trans[cube_test.piece_3.front], color_trans[cube_test.piece_7.front]], (0, -1, 0)),
            'u': ([color_trans[cube_test.piece_5.up], color_trans[cube_test.piece_4.up], color_trans[cube_test.piece_7.up], color_trans[cube_test.piece_6.up]], (0, 0, 1)),
            'd': ([color_trans[cube_test.piece_0.down], color_trans[cube_test.piece_1.down], color_trans[cube_test.piece_2.down], color_trans[cube_test.piece_3.down]], (0, 0, -1))
        }

stickers = []

for face_color, axis in faces.values():
    i = 0
    for x in (-0.5, 0.5):
        for y in (-0.5, 0.5):
            sticker = box(color=face_color[i], pos=(x, y, 1),
                    length = 0.98, height = 0.98, width = 0.05)
            cos_angle = dot((0, 0, 1), axis)
            pivot = (cross((0, 0, 1), axis) if cos_angle == 0 else (1, 0, 0))
            sticker.rotate(angle = acos(cos_angle), axis = pivot, origin = (0, 0, 0))
            stickers.append(sticker)
            i += 1

while True and steps:
    key = scene.kb.getkey()
    if key.lower() in faces:
        face_color, axis= faces[key.lower()]
        angle = ((pi / 2) if key.isupper() else -pi / 2)
        for r in arange(0, angle, angle/fps):
            rate(fps)
            for sticker in stickers:
                if dot(sticker.pos, axis) >= 0.4:
                    sticker.rotate(angle = angle/fps, axis = axis, origin = (0, 0, 0))


