import random

import matplotlib.pyplot as plt
import numpy as np


def writeFile(size, x2Bigger = False):
    points = []
    value = [-1, 1]

    for i in range(1, size):

        x2 = random.uniform(0, 1)
        if x2Bigger:
            while x2 < 0.5:
                x2 = random.uniform(0, 1)

        points.append([
            random.uniform(0, 1),
            x2,
            value[random.randint(0, 1)]
        ])

    np.savetxt("file.txt", np.array(points), fmt="%s")


def readFile():
    file = open('file.txt', "r")
    lines = file.readlines()
    file.close()

    blue1 = []
    blue2 = []
    red1 = []
    red2 = []

    for line in lines:
        v = line.split(' ')

        if int(v[2].rstrip(('.0\n'))) == 1:
            blue1.append(float(v[0]))
            blue2.append(float(v[1]))
        else:
            red1.append(float(v[0]))
            red2.append(float(v[1]))

    plt.scatter(blue1, blue2, color="blue")
    plt.scatter(red1, red2, color="red")
    plt.show()

    formatedLines = []

    for line in lines:
        line = line.split(' ')
        formatedLines.append([
            float(line[0]),
            float(line[1]),
            float(line[2])
        ])

    return formatedLines