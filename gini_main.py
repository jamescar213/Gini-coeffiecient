import pandas as pd
import datetime as dt

def data_sorted(filepath):

    df = pd.read_csv(filepath, skiprows=3)
    df.columns = df.columns.str.strip()  #removing any leading/trailing whitespace from column names

    df_long = df.melt(id_vars=["Country Name", "Country Code"], var_name="Year", value_name="Gini Index") 

    df_long = df_long[df_long["Year"].str.isnumeric()] 
    df_long = df_long.dropna(subset =["Gini Index"]) #dropping rows with missing Gini Index values
    df_long = df_long.sort_values(["Country Name", "Year"]) #sorting by country and year
    
    return df_long






