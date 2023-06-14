from data import importData
from approximation import lagrangeApproximation

if __name__ == '__main__':
    distance, height, title = importData('WielkiKanionKolorado.csv')
    lagrangeApproximation(distance, height, title, 5)
    lagrangeApproximation(distance, height, title, 10)
    lagrangeApproximation(distance, height, title, 15)
    lagrangeApproximation(distance, height, title, 20)
