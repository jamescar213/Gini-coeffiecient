import pandas as pd
import matplotlib.pyplot as plt
from gini_main import data_sorted

data = data_sorted("world_bank_gini_csv.csv")


def gini_change(df, country):
    subset = df[df["Country Name"] == country].copy()

    #converting Year and Gini Index to numeric types
    subset["Year"] = pd.to_numeric(subset["Year"], errors="coerce")
    subset["Gini Index"] = pd.to_numeric(subset["Gini Index"], errors='coerce')

    #dropping any missing numeric data
    subset = subset.dropna(subset=["Year", "Gini Index"])

    if subset.empty:
        print(f"No data available for {country}.")
        return
    print(subset.dtypes.head())

   
    plt.figure(figsize=(10, 6))
    plt.plot(subset["Year"], subset["Gini Index"], marker='2', linestyle="-")
    plt.title(f"Gini Index Over Time for {country}")
    plt.xlabel("Year")
    plt.ylabel("Gini Index")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    
#example 
gini_change(data, "United States")



    



