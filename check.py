import matplotlib.pyplot as plt


graph1 = {'x': [],
          'y': []}
graph2 = {'x': [],
          'y': []}

with open('graphs.txt', 'r') as file:
    for line in file:
        data_arr = line.replace('\t', ' ').replace('\n', '').split(' ')
        graph1['x'].append(float(data_arr[0]))
        graph1['y'].append(float(data_arr[1]))

        graph2['x'].append(float(data_arr[0]))
        graph2['y'].append(float(data_arr[2]))

plt.plot(graph2['x'], graph2['y'])
plt.xlabel("Частота сигнала")
plt.show()



