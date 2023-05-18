import pandas as pd
import matplotlib.pyplot as plt

def importData(file_name):
    data = pd.read_csv(file_name)
    distance = data['Dystans (m)']
    height = data['Wysokość (m)']
    plt.plot(distance, height)
    plt.xlabel('Dystans (m)')
    plt.ylabel('Wysokość (m)')
    title = file_name.split('.')[0]
    title = ''.join([' ' + char if char.isupper() else char for char in title]).strip()
    plt.title(title)
    plt.show()
    return data
