import numpy
import matplotlib.pyplot as plt
from cv2 import imread, IMREAD_GRAYSCALE, THRESH_BINARY, moments, HuMoments, threshold
from math import copysign, log10
from db_util import saveImg, searchRunes

def calcHuMoments(filename):
    im = imread(filename, IMREAD_GRAYSCALE)
    # Threshold image
    _,im = threshold(im, 128, 255, THRESH_BINARY)
    # Calculate Moments
    _moments = moments(im)
    # Calculate Hu Moments
    huMoments = HuMoments(_moments)
    # Log scale hu moments
    for i in range(0,7):
        huMoments[i] = -1* copysign(1.0, huMoments[i]) * log10(abs(huMoments[i]))

    return huMoments

def identifyImg(filename):
    huMoments = calcHuMoments(filename)

def addImg(filename, name, description):
    huMoments = calcHuMoments(filename)
    saveImg(name, description, huMoments)