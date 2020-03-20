import numpy
import matplotlib.pyplot as plt
from cv2 import imread, IMREAD_GRAYSCALE, THRESH_BINARY, moments, HuMoments, threshold
from math import copysign, log10, sqrt, pow
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
    runes = searchRunes()
    results = []
    for rune in runes:
        score = calcScore(rune, huMoments)
        results.append([rune[0], rune[1], score])

    results.sort()
    print(results)
    return calcBestResult(results)

def addImg(filename, idRuneInfo):
    huMoments = calcHuMoments(filename)
    saveImg(idRuneInfo, huMoments)
    return huMoments

def calcScore(rune, huMoments):
    score = sqrt(
        pow(huMoments[0] - rune[2], 2) +
        pow(huMoments[1] - rune[3], 2) +
        pow(huMoments[2] - rune[4], 2) +
        pow(huMoments[3] - rune[5], 2) +
        pow(huMoments[4] - rune[6], 2) +
        pow(huMoments[5] - rune[7], 2) +
        pow(huMoments[6] - rune[8], 2)
    )
    return score

def calcBestResult(results):
    best = [results[0][0], abs(results[0][2])]
    for result in results:
        if abs(result[2]) < best[1]:
            best[0] = result[0]
            best[1] = result[2]
    return best