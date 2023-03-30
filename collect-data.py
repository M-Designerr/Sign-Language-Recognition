import cv2
import numpy as np
import os
import string

# Create data directory structure
if not os.path.exists("raw_data"):
    os.makedirs("raw_data")

for i in range(10):
    if not os.path.exists("raw_data/" + str(i)):
        os.makedirs("raw_data/"+str(i))

for i in string.ascii_uppercase:
    if not os.path.exists("raw_data/" + i):
        os.makedirs("raw_data/"+i)


# Training data
directory = 'raw_data/'
minValue = 75

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)

    # Getting count of existing images
    count = {
        'zero': len(os.listdir(directory+"/0")),
        'one': len(os.listdir(directory+"/1")),
        'two': len(os.listdir(directory+"/2")),
        'three': len(os.listdir(directory+"/3")),
        'four': len(os.listdir(directory+"/4")),
        'five': len(os.listdir(directory+"/5")),
        'six': len(os.listdir(directory+"/6")),
        'seven': len(os.listdir(directory+"/7")),
        'eight': len(os.listdir(directory+"/8")),
        'nine': len(os.listdir(directory+"/9")),
        'a': len(os.listdir(directory+"/A")),
        'b': len(os.listdir(directory+"/B")),
        'c': len(os.listdir(directory+"/C")),
        'd': len(os.listdir(directory+"/D")),
        'e': len(os.listdir(directory+"/E")),
        'f': len(os.listdir(directory+"/F")),
        'g': len(os.listdir(directory+"/G")),
        'h': len(os.listdir(directory+"/H")),
        'i': len(os.listdir(directory+"/I")),
        'j': len(os.listdir(directory+"/J")),
        'k': len(os.listdir(directory+"/K")),
        'l': len(os.listdir(directory+"/L")),
        'm': len(os.listdir(directory+"/M")),
        'n': len(os.listdir(directory+"/N")),
        'o': len(os.listdir(directory+"/O")),
        'p': len(os.listdir(directory+"/P")),
        'q': len(os.listdir(directory+"/Q")),
        'r': len(os.listdir(directory+"/R")),
        's': len(os.listdir(directory+"/S")),
        't': len(os.listdir(directory+"/T")),
        'u': len(os.listdir(directory+"/U")),
        'v': len(os.listdir(directory+"/V")),
        'w': len(os.listdir(directory+"/W")),
        'x': len(os.listdir(directory+"/X")),
        'y': len(os.listdir(directory+"/Y")),
        'z': len(os.listdir(directory+"/Z"))
    }

    # Printing the count in each set to the screen
    cv2.putText(frame, "IMAGE COUNT", (10, 60),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "ZERO : "+str(count['zero']),
                (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "ONE : "+str(count['one']), (10, 80),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "TWO : "+str(count['two']), (10, 90),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "THREE : "+str(count['three']),
                (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "FOUR : "+str(count['four']),
                (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "FIVE : "+str(count['five']),
                (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "SIX : "+str(count['six']), (10, 130),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "SEVEN : "+str(count['seven']), (10, 140),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "EIGHT : "+str(count['eight']), (10, 150),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "NINE : "+str(count['nine']), (10, 160),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)

    cv2.putText(frame, "a : "+str(count['a']), (10, 170),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "b : "+str(count['b']), (10, 180),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "c : "+str(count['c']), (10, 190),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "d : "+str(count['d']), (10, 200),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "e : "+str(count['e']), (10, 210),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "f : "+str(count['f']), (10, 220),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "g : "+str(count['g']), (10, 230),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "h : "+str(count['h']), (10, 240),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "i : "+str(count['i']), (10, 250),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "j : "+str(count['j']), (10, 260),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "k : "+str(count['k']), (10, 270),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "l : "+str(count['l']), (10, 280),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "m : "+str(count['m']), (10, 290),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "n : "+str(count['n']), (10, 300),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "o : "+str(count['o']), (10, 310),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "p : "+str(count['p']), (10, 320),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "q : "+str(count['q']), (10, 330),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "r : "+str(count['r']), (10, 340),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "s : "+str(count['s']), (10, 350),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "t : "+str(count['t']), (10, 360),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "u : "+str(count['u']), (10, 370),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "v : "+str(count['v']), (10, 380),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "w : "+str(count['w']), (10, 390),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "x : "+str(count['x']), (10, 400),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "y : "+str(count['y']), (10, 410),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "z : "+str(count['z']), (10, 420),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)

    # Coordinates of the ROI
    # r = cv2.selectROI("select the area", frame)
    # print('Selected bounding boxes: {}'.format(r))
    # 320, 10, 620, 310 = r

    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (320-1, 10-1), (620+1, 310+1), (255, 0, 0), 1)

    # Extracting the ROI
    roi = frame[10:310, 320:620]

    cv2.imshow("Frame", frame)

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 2)

    test_img = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    test_img = cv2.resize(test_img, (300, 300))
    cv2.imshow("test", test_img)

    interrupt = cv2.waitKey(1)
    if interrupt % 256 == 27:  # esc key
        break
    if interrupt == ord('0'):
        cv2.imwrite(directory+'0/'+str(count['zero'])+'.jpg', roi)
    if interrupt % 256 == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['one'])+'.jpg', roi)
    if interrupt % 256 == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg', roi)
    if interrupt % 256 == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg', roi)
    if interrupt % 256 == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg', roi)
    if interrupt % 256 == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['five'])+'.jpg', roi)
    if interrupt % 256 == ord('6'):
        cv2.imwrite(directory+'6/'+str(count['six'])+'.jpg', roi)
    if interrupt % 256 == ord('7'):
        cv2.imwrite(directory+'7/'+str(count['seven'])+'.jpg', roi)
    if interrupt % 256 == ord('8'):
        cv2.imwrite(directory+'8/'+str(count['eight'])+'.jpg', roi)
    if interrupt % 256 == ord('9'):
        cv2.imwrite(directory+'9/'+str(count['nine'])+'.jpg', roi)

    if interrupt % 256 == ord('a'):
        cv2.imwrite(directory+'A/'+str(count['a'])+'.jpg', roi)
    if interrupt % 256 == ord('b'):
        cv2.imwrite(directory+'B/'+str(count['b'])+'.jpg', roi)
    if interrupt % 256 == ord('c'):
        cv2.imwrite(directory+'C/'+str(count['c'])+'.jpg', roi)
    if interrupt % 256 == ord('d'):
        cv2.imwrite(directory+'D/'+str(count['d'])+'.jpg', roi)
    if interrupt % 256 == ord('e'):
        cv2.imwrite(directory+'E/'+str(count['e'])+'.jpg', roi)
    if interrupt % 256 == ord('f'):
        cv2.imwrite(directory+'F/'+str(count['f'])+'.jpg', roi)
    if interrupt % 256 == ord('g'):
        cv2.imwrite(directory+'G/'+str(count['g'])+'.jpg', roi)
    if interrupt % 256 == ord('h'):
        cv2.imwrite(directory+'H/'+str(count['h'])+'.jpg', roi)
    if interrupt % 256 == ord('i'):
        cv2.imwrite(directory+'I/'+str(count['i'])+'.jpg', roi)
    if interrupt % 256 == ord('j'):
        cv2.imwrite(directory+'J/'+str(count['j'])+'.jpg', roi)
    if interrupt % 256 == ord('k'):
        cv2.imwrite(directory+'K/'+str(count['k'])+'.jpg', roi)
    if interrupt % 256 == ord('l'):
        cv2.imwrite(directory+'L/'+str(count['l'])+'.jpg', roi)
    if interrupt % 256 == ord('m'):
        cv2.imwrite(directory+'M/'+str(count['m'])+'.jpg', roi)
    if interrupt % 256 == ord('n'):
        cv2.imwrite(directory+'N/'+str(count['n'])+'.jpg', roi)
    if interrupt % 256 == ord('o'):
        cv2.imwrite(directory+'O/'+str(count['o'])+'.jpg', roi)
    if interrupt % 256 == ord('p'):
        cv2.imwrite(directory+'P/'+str(count['p'])+'.jpg', roi)
    if interrupt % 256 == ord('q'):
        cv2.imwrite(directory+'Q/'+str(count['q'])+'.jpg', roi)
    if interrupt % 256 == ord('r'):
        cv2.imwrite(directory+'R/'+str(count['r'])+'.jpg', roi)
    if interrupt % 256 == ord('s'):
        cv2.imwrite(directory+'S/'+str(count['s'])+'.jpg', roi)
    if interrupt % 256 == ord('t'):
        cv2.imwrite(directory+'T/'+str(count['t'])+'.jpg', roi)
    if interrupt % 256 == ord('u'):
        cv2.imwrite(directory+'U/'+str(count['u'])+'.jpg', roi)
    if interrupt % 256 == ord('v'):
        cv2.imwrite(directory+'V/'+str(count['v'])+'.jpg', roi)
    if interrupt % 256 == ord('w'):
        cv2.imwrite(directory+'W/'+str(count['w'])+'.jpg', roi)
    if interrupt % 256 == ord('x'):
        cv2.imwrite(directory+'X/'+str(count['x'])+'.jpg', roi)
    if interrupt % 256 == ord('y'):
        cv2.imwrite(directory+'Y/'+str(count['y'])+'.jpg', roi)
    if interrupt % 256 == ord('z'):
        cv2.imwrite(directory+'Z/'+str(count['z'])+'.jpg', roi)

cap.release()
cv2.destroyAllWindows()
