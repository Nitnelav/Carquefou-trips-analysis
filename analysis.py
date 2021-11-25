import pandas as pd

trips_file_default = "trips_default.csv"
trips_file_sncf = "trips_sncf.csv"

df_trips_default = pd.read_csv(trips_file_default, sep=";")
df_trips_sncf = pd.read_csv(trips_file_sncf, sep=";")

print(df_trips_default["modes"].value_counts())
print(df_trips_sncf["modes"].value_counts())