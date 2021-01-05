import random

import matplotlib.pyplot as plt

from file import readFile, writeFile


def getRandomPoint(lines):
    line = lines[random.randint(0, len(lines)) - 1].split(' ')
    return [
        float(line[0]),
        float(line[1]),
        float(line[2])
    ]

def initNeuron():
    weights = []

    for _ in range(1, 3):
        weights.append(random.randint(0, 1))

    return {
        'biais': 0.5,
        'out': 0,
        'weights': weights
    }

def getValueNeuron(neuron, x0, x1):
    w = neuron.get('weights')
    teta = (w[0] * x0) + (w[1] * x1) - neuron.get('biais')

    if teta > 0:
        return 1
    else:
        return -1


def trainNeuron(numberIteration, showGraph = False):
    n1 = initNeuron()
    x = []
    y = []

    for i in range(1, numberIteration):

        error = 0

        for line in lines:

            res = getValueNeuron(n1, line[0], line[1])

            if n1['out'] != res:
                error = error + 1

            n1['out'] = res
            n1 = updateNeuron(n1, line[0], line[1], line[2])

        print(error)
        y.append(error)
        x.append(i)

    if showGraph:
        plt.plot(x, y)
        plt.show()


def updateNeuron(neuron, x1, x2, tag):
    newBiais = neuron.get('biais') + step * (tag * neuron.get('out')) * -0.5
    newW1 = neuron.get('weights')[0] + step * (tag * neuron.get('out')) * x1
    newW2 = neuron.get('weights')[1] + step * (tag * neuron.get('out')) * x2

    neuron['biais'] = newBiais
    neuron['weights'] = [newW1, newW2]

    return neuron


if __name__ == '__main__':
    size = 100
    step = 0.01
    random.seed(15)

    x2BiggerThan0_5 = False
    # A mettre a true si x2 >0.5
    writeFile(size, x2BiggerThan0_5)

    lines = readFile()

    trainNeuron(5,True)
    trainNeuron(10,True)
    trainNeuron(50,True)
    trainNeuron(100,True)


