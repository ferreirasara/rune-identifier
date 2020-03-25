import numpy
import matplotlib.pyplot as plt
from cv2 import imread, IMREAD_GRAYSCALE, THRESH_BINARY, moments, HuMoments, threshold, Canny, cornerHarris, dilate
from math import copysign, log10, sqrt, pow

filename1 = "img\\fehu.jpg"
filename2 = "img\\fehu\\3.jpg"

def _edges(filename):
    im = imread(filename)
    print(filename)
    try:
        edges = Canny(im,100,200)
        return edges
    except Exception as e:
        print(e)

def _corners(filename):
    im = imread(filename)
    print(filename)
    try:
        dst = cornerHarris(im,2,3,0.04)
        dst = dilate(dst, None)
        im[dst>0.01*dst.max()]=[0,0,255]
        return im
    except Exception as e:
        print(e)

edges1 = _edges(filename1)
edges2 = _edges(filename2)
corners1 = _corners(filename1)
# corners2 = _corners(filename2)

plt.figure()

plt.subplot(2,2,1)
plt.imshow(edges1, cmap=plt.cm.gray)
plt.subplot(2,2,2)
plt.imshow(edges2, cmap=plt.cm.gray)

# plt.subplot(2,2,1)
# plt.imshow(corners1, cmap=plt.cm.gray)
# plt.subplot(2,2,2)
# plt.imshow(corners1, cmap=plt.cm.gray)

plt.show()