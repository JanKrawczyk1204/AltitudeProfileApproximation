import random
import matplotlib.pyplot as plt
from scipy.linalg import lu_solve, lu_factor
import numpy as np


def lagrangeApproximation(distance, height, name, points, regular=True):
    step = int(len(distance) / points)
    x = [i for i in range(0, int(distance[-1]))]  # Modified line
    y = []
    use_distance = []
    use_height = []

    if regular:
        use_distance = distance[::step]
        use_height = height[::step]
    else:
        los = []
        for i in range(0, points):
            los.append(random.randint(1, len(distance)))
            los.sort()
        for i in los:
            use_distance.append(distance[i])
            use_height.append(height[i])

    for xp in x:
        yp = 0
        for i in range(len(use_distance)):
            p = 1
            for j in range(len(use_distance)):
                if i != j:
                    p = p * (xp - use_distance[j]) / (use_distance[i] - use_distance[j])
            yp = yp + p * use_height[i]
        y.append(yp)

    plt.plot(x, y, label="Lagrange's interpolation")
    plt.plot(distance, height, label="Height profile")
    plt.scatter(use_distance, use_height)
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title(str(name) + " Lagrange's interpolation, points = " + str(points))
    plt.legend()
    plt.show()
    return x, y

def cubicInterpolation(distance, height, name, points, regular=True):
    all_points = list(zip(distance, height))
    chosen_points = []
    if regular:
        indices = np.linspace(0, len(distance) - 1, points, dtype=int)
        chosen_points = [all_points[i] for i in indices]
    else:
        los = []
        los.append(0)
        for i in range(0, points - 2):
            los.append(random.randint(1, len(distance)))
            los.sort()
        los.append(len(distance) - 1)
        for i in los:
            chosen_points.append(all_points[i])
    x = [point[0] for point in chosen_points]
    y = [point[1] for point in chosen_points]
    spline_func = splineInterpolation(chosen_points)
    x_values = np.linspace(min(distance), max(distance), num=1000)
    plt.plot(x_values, [spline_func(xi) for xi in x_values], label="Cubic spline interpolation")
    plt.plot(distance, height, label="Height profile")
    plt.scatter(x, y)
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title(str(name) + " Cubic spline interpolation, points = " + str(points))
    plt.legend()
    plt.show()
    return x, y


def splineInterpolation(points):
    def calculateParams():
        n = len(points)
        A = np.zeros((4 * (n - 1), 4 * (n - 1)))
        b = np.zeros((4 * (n - 1), 1))
        for i in range(n - 1):
            x, y = points[i]
            row = np.zeros((4 * (n - 1)))
            row[4 * i + 3] = 1
            A[4 * i + 3] = row
            b[4 * i + 3] = (float(y))
        for i in range(n - 1):
            x1, y1 = points[i + 1]
            x0, y0 = points[i]
            h = float(x1) - float(x0)
            row = np.zeros((4 * (n - 1)))
            row[4 * i] = h ** 3
            row[4 * i + 1] = h ** 2
            row[4 * i + 2] = h ** 1
            row[4 * i + 3] = 1
            A[4 * i + 2] = row
            b[4 * i + 2] = float(y1)
        for i in range(n - 2):
            x1, y1 = points[i + 1]
            x0, y0 = points[i]
            h = float(x1) - float(x0)
            row = np.zeros((4 * (n - 1)))
            row[4 * i] = 3 * (h ** 2)
            row[4 * i + 1] = 2 * h
            row[4 * i + 2] = 1
            row[4 * (i + 1) + 2] = -1
            A[4 * i] = row
            b[4 * i] = float(0)
        for i in range(n - 2):
            x1, y1 = points[i + 1]
            x0, y0 = points[i]
            h = float(x1) - float(x0)
            row = np.zeros((4 * (n - 1)))
            row[4 * i] = 6 * h
            row[4 * i + 1] = 2
            row[4 * (i + 1) + 1] = -2
            A[4 * (i + 1) + 1] = row
            b[4 * (i + 1) + 1] = float(0)
        row = np.zeros((4 * (n - 1)))
        row[1] = 2
        A[1] = row
        b[1] = float(0)
        row = np.zeros((4 * (n - 1)))
        x1, y1 = points[-1]
        x0, y0 = points[-2]
        h = float(x1) - float(x0)
        row[1] = 2
        row[-4] = 6 * h
        A[-4] = row
        b[-4] = float(0)
        result = lu_solve(lu_factor(A), b)
        return result

    params = calculateParams()
    def f(x):
        param_array = []
        row = []
        for param in params:
            row.append(param)
            if len(row) == 4:
                param_array.append(row.copy())
                row.clear()

        for i in range(1, len(points)):
            xi, yi = points[i - 1]
            xj, yj = points[i]
            if float(xi) <= x <= float(xj):
                a, b, c, d = param_array[i - 1]
                h = x - float(xi)
                return a * (h ** 3) + b * (h ** 2) + c * h + d

        return -123

    return f
