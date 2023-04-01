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
if not os.path.exists("data_alpha"):
    os.makedirs("data_alpha")
if not os.path.exists("data_alpha/train"):
    os.makedirs("data_alpha/train")
if not os.path.exists("data_alpha/test"):
    os.makedirs("data_alpha/test")

if not os.path.exists("data_digit"):
    os.makedirs("data_digit")
if not os.path.exists("data_digit/train"):
    os.makedirs("data_digit/train")
if not os.path.exists("data_digit/test"):
    os.makedirs("data_digit/test")

path = "raw_data_alpha"
path0 = "raw_data_digit"
path1 = "data_alpha"
path2 = "data_digit"
a = ['label']

for i in range(64*64):
    a.append("pixel"+str(i))


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

label1 = 0
var1 = 0
c11 = 0
c21 = 0

for (dirpath, dirnames, filenames) in os.walk(path0):
    for dirname in dirnames:
        print(dirname)
        for (direcpath, direcnames, files) in os.walk(path0+"/"+dirname):
            if not os.path.exists(path2+"/train/"+dirname):
                os.makedirs(path2+"/train/"+dirname)
            if not os.path.exists(path2+"/test/"+dirname):
                os.makedirs(path2+"/test/"+dirname)
            num = 0.75*len(files)
            i = 0
            for file in files:
                var1 += 1
                actual_path = path0+"/"+dirname+"/"+file
                actual_path1 = path2+"/"+"train/"+dirname+"/"+file
                actual_path2 = path2+"/"+"test/"+dirname+"/"+file
                img = cv2.imread(actual_path, 0)
                bw_image = func(actual_path)
                if i < num:
                    c11 += 1
                    cv2.imwrite(actual_path1, bw_image)
                else:
                    c21 += 1
                    cv2.imwrite(actual_path2, bw_image)

                i = i+1

        label1 = label1+1


print(var1)
print(c11)
print(c21)
