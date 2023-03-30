import numpy as np
import cv2
import os

minValue = 75


# image processing function to convert image to
# black and white outline using Gaussian adaptive thresholding
def func(path):
    frame = cv2.imread(path)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 2)

    res = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    return res


# Create the directory structure
if not os.path.exists("data2"):
    os.makedirs("data2")
if not os.path.exists("data2/train"):
    os.makedirs("data2/train")
if not os.path.exists("data2/test"):
    os.makedirs("data2/test")
path = "data"
path1 = "data2"
a = ['label']

for i in range(64*64):
    a.append("pixel"+str(i))


#outputLine = a.tolist()


label = 0
var = 0
c1 = 0
c2 = 0

for (dirpath, dirnames, filenames) in os.walk(path):
    for dirname in dirnames:
        print(dirname)
        for (direcpath, direcnames, files) in os.walk(path+"/"+dirname):
            if not os.path.exists(path1+"/train/"+dirname):
                os.makedirs(path1+"/train/"+dirname)
            if not os.path.exists(path1+"/test/"+dirname):
                os.makedirs(path1+"/test/"+dirname)
            num = 0.75*len(files)
            i = 0
            for file in files:
                var += 1
                actual_path = path+"/"+dirname+"/"+file
                actual_path1 = path1+"/"+"train/"+dirname+"/"+file
                actual_path2 = path1+"/"+"test/"+dirname+"/"+file
                img = cv2.imread(actual_path, 0)
                bw_image = func(actual_path)
                if i < num:
                    c1 += 1
                    cv2.imwrite(actual_path1, bw_image)
                else:
                    c2 += 1
                    cv2.imwrite(actual_path2, bw_image)

                i = i+1

        label = label+1
print(var)
print(c1)
print(c2)
