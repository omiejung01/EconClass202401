import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def case06():
    x = np.arange(-10, 11)
    y = x ** 2
    #plt.plot(x, y)
    #plt.show()
    #print(x)
    #print(y

    y_2 = -x ** 2
    #plt.plot(x, y, "-")
    #plt.plot(x, y_2, "-")
    #plt.show()

    #plt.plot(x, y, color="red")
    #plt.plot(x, y, linewidth=8, color="red")
    #plt.plot(x, y, color="red", linewidth=8)
    #plt.plot(x, y, "--")
    #plt.plot(x, y, "--",color="red", linewidth=8)
    #plt.plot(x, y, "o")
    #plt.plot(x, y_2, color="#A727F5")
    #plt.show()

    plt.plot(x, y, marker="o", markerfacecolor="red", markersize=10)
    plt.show()


def case07():
    #Scatter plot
    x = np.random.rand(30)
    y = np.random.rand(30)
    z = np.random.rand(30)
    colours = np.random.choice(["blue", "black", "red"], 30)
    plt.scatter(x, y, marker="o", color=colours, s=z * 100)
    plt.show()

def case08():
    # Histogram
    x = np.random.randn(1000)
    bins = np.arange(-4, 4, 0.5)
    plt.hist(x, edgecolor='white', linewidth=1.5, bins=bins)
    #plt.hist(x)
    plt.show()


def case09():
    #Bar chart
    #pays = ["France", "Italie", "Belgique", "Allemagne"]
    #unemployment = [9.3, 9.7, 6.5, 3.4]
    #plt.bar(pays, unemployment)
    #plt.barh(pays, unemployment)
    #plt.show()

    #several series
    countries = ["France", "Italie", "Belgique", "Allemagne"]
    unemp_f = [9.1, 11.2, 6.4, 2.9]
    unemp_h = [9.5, 9, 6.6, 3.8]
    # Position on the x-axis for each label
    position = np.arange(len(countries))

    # Bar widths
    width = .35
    # Creating the figure and a set of subgraphics
    fig, ax = plt.subplots()
    r1 = ax.bar(position - width/2, unemp_f, width)
    r2 = ax.bar(position + width/2, unemp_h, width)
    # Modification of the marks on the x-axis and their labels
    ax.set_xticks(position)
    ax.set_xticklabels(countries)

    plt.show()


def case10():
    countries = ["France", "Italie", "Belgique", "Allemagne"]
    no_unemp_f = [1.307, 1.185, .577, .148]
    no_unemp_h = [1.46, 1.338, .878, .179]
    #plt.bar(countries, no_unemp_f)
    #plt.bar(countries, no_unemp_h, bottom=no_unemp_f)
    #plt.show()

    x = np.arange(-10, 11)
    y = x ** 2
    y_2 = x ** 3
    plt.plot(x, y, label="square ($x^2$)")
    plt.plot(x, y_2, label="cube ($x^3$)")
    plt.legend()
    plt.legend()
    path = 'C:\\data\\output\\' + 'mychart.png'
    plt.savefig(path)





if __name__ == '__main__':
    #case06()
    #case07()
    #case08()
    #case09()
    case10()

