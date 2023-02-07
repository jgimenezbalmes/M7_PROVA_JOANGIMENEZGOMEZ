import pandas as pd
import matplotlib.pyplot as plt

def ex1():
    a = pd.read_csv("llistat.csv")
    b = a.dropna()
    b = b.groupby("NAME").mean()
    plt.bar(b.index, b.NOTES)
    plt.title("JOAN GIMENEZ GOMEZ")
    plt.xlabel("ALUMNAT")
    plt.ylabel("NOTES")
    plt.show()