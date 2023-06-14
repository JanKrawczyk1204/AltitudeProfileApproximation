import matplotlib.pyplot as plt


def lagrangeApproximation(distance, height, name, points):
    step = int(len(distance)/points)
    x = [i for i in range(0, int(distance[-1]) + 1)]
    y = []
    use_distance = distance[::step]
    use_height = height[::step]
    for xp in x:
        yp = 0
        for i in range(len(use_distance)):
            p = 1
            for j in range(len(use_distance)):
                if i != j:
                    p = p * (xp - use_distance[j]) / (use_distance[i] - use_distance[j])
            yp = yp + p * use_height[i]
        y.append(yp)
    plt.plot(x, y, label="Lagrange'a interpolation")
    plt.plot(distance, height, label="height profile")
    plt.scatter(use_distance, use_height)
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title(str(name) + " Lagrange's interpolation, points = " + str(points))
    plt.legend()
    plt.show()
    return x, y


def interpolate_with_spline(distance, height, name, points):
    step = int(len(distance) / points)
    x = [i for i in range(0, int(distance[-1]) + 1)]
    y = []
    use_distance = distance[::step]
    use_height = height[::step]
    #TODO aproksymacja

    plt.plot(x, y, label="Lagrange'a interpolation")
    plt.plot(distance, height, label="height profile")
    plt.scatter(use_distance, use_height)
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title(str(name) + " Lagrange's interpolation, points = " + str(points))
    plt.legend()
    plt.show()
    return x, y