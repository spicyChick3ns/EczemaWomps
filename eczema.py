#Melissa Gonzales
#February 01 2017
#This program reads from an excel sheet that contains logged data of my eczema
import pandas as pd
import matplotlib.pyplot as plt
def main():
    df  = pd.read_excel(r"EczemaProgress.xlsx", sheetname=0)
    date = df[["Date"]]
    a=df.plot()

    a.set_xlabel("Date")
    a.set_xticklabels(df.Date, rotation=-10)
    a.set_ylabel("Temperature (Celsius)")
    a.set_title("Eczema Progress 2016")
    b=df.ewm(span=15).mean().plot()
    b.set_xlabel("Date")
    b.set_xticklabels(df.Date, rotation=-10)
    b.set_ylabel("Temperature (Celsius)")
    b.set_title("Rolling Average: Eczema 2016")

    plt.show()


main()
