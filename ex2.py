import pandas as pd
import matplotlib.pyplot as plt

def ex2():
    a = pd.read_csv("llistat.csv")
    b = a.dropna()
    b = b.loc[b['GROUP']=='DAW2']
    b = b.groupby("MODULE").head(20)
    c = b.loc[b['MODULE']=='M07']
    c = c.sort_values(by="NAME")
    d = b.loc[b['MODULE']=='M08']
    d = d.sort_values(by="NAME")
    plt.plot(c.NAME, c.ABSENCES, 'o-k')
    plt.plot(d.NAME, d.ABSENCES, 'xr--')
    plt.title("JOAN GIMENEZ GOMEZ")
    plt.xlabel("ALUMNAT")
    plt.ylabel("Faltes en %")
    plt.legend(['M07', 'M08'])
    plt.show()


