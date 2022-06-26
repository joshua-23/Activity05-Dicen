import cv2 as cv
import numpy as np
from os import system
from time import sleep


system('cls')

filepath = "Eimi.jpg"

img = cv.imread(filepath)


if len(img.shape) < 3:
    print("Image is grayscale")
    sleep(3)
    exit()


system('cls')
shp = img.shape
print("Access a pixel")
ekis = int(input("Enter 'X' coordinate value (max value "+str(shp[0])+" ) : "))
ways = int(input("Enter 'Y' coordinate value (max value "+str(shp[1])+" ) : "))
tyanel = int(input("""Select channel:
0 - blue
1 - green
2 - red
>> """))

akses = img.item(ekis, ways, tyanel)

system('cls')
sheyp = img.shape
print("Modify a pixel")
ekis = int(input("Enter 'x' coordinate value (max value "+str(shp[0])+" ) : "))
ways = int(input("Enter 'y' coordinate value (max value "+str(shp[1])+" ) : "))
asul = int(input("Enter blue channel value: "))
berde = int(input("Enter green channel value: "))
pula = int(input("Enter red channel value: "))

system('cls')

print("Outputs:")

print("\nAccessed Pixel Value:", akses)

print("Pixel value before modify:", img[ekis, ways])  


img.itemset((ekis, ways, 0), asul)
img.itemset((ekis, ways, 1), berde)
img.itemset((ekis, ways, 2), pula)

print("Pixel value after modified:", img[ekis, ways])  


wids = 640
hayts = 427

if wids > shp[1] or hayts > shp[0]:
    print("Set Image Dimension: Out of bounderies")
else:
    print("Set Image Dimension: Within the bounderies")


pix = 1683001

if pix > img.size: print("Set Pixel: Higher than the pixel count")
elif pix < img.size: print("Set Pixel: Lower than the pixel count")
else: print("Set pixel: Equal to the pixel count")

print("Image Data Type:", img.dtype)