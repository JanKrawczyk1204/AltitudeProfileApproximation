from data import importData
from approximation import lagrangeApproximation, cubicInterpolation

if __name__ == '__main__':
    distance, height, title = importData('WielkiKanionKolorado.csv')
    cubicInterpolation(distance, height, title, 20)
    cubicInterpolation(distance, height, title, 20, False)

